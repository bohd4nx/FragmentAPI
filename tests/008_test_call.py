"""Check raw Fragment API calls and transport error handling."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from curl_cffi.requests import AsyncSession, Response

from pyfragment import FragmentClient, FragmentPageError
from pyfragment.core.transport import get_fragment_hash, fragment_request
from tests.shared import FAKE_HASH, FAKE_RESPONSE

# client.call() mocked tests


@pytest.mark.asyncio
async def test_call_returns_api_response(client: FragmentClient) -> None:
    with (
        patch("pyfragment.domains.base.get_fragment_hash", AsyncMock(return_value=FAKE_HASH)),
        patch("pyfragment.domains.base.fragment_request", AsyncMock(return_value=FAKE_RESPONSE)),
    ):
        result = await client.call("anyMethod", {"key": "value"})

    assert result == FAKE_RESPONSE


@pytest.mark.asyncio
async def test_call_default_page_url(client: FragmentClient) -> None:
    with (
        patch("pyfragment.domains.base.get_fragment_hash", AsyncMock(return_value=FAKE_HASH)),
        patch("pyfragment.domains.base.fragment_request", AsyncMock(return_value=FAKE_RESPONSE)),
    ):
        result = await client.call("anyMethod")

    assert result == FAKE_RESPONSE


@pytest.mark.asyncio
async def test_call_no_data(client: FragmentClient) -> None:
    mock_request = AsyncMock(return_value={})

    with (
        patch("pyfragment.domains.base.get_fragment_hash", AsyncMock(return_value=FAKE_HASH)),
        patch("pyfragment.domains.base.fragment_request", mock_request),
    ):
        await client.call("anyMethod")

    _, _, _, sent_data = mock_request.call_args.args
    assert sent_data == {"method": "anyMethod"}


@pytest.mark.asyncio
async def test_call_merges_extra_data(client: FragmentClient) -> None:
    mock_request = AsyncMock(return_value={})

    with (
        patch("pyfragment.domains.base.get_fragment_hash", AsyncMock(return_value=FAKE_HASH)),
        patch("pyfragment.domains.base.fragment_request", mock_request),
    ):
        await client.call("anyMethod", {"key": "value", "num": 7})

    _, _, _, sent_data = mock_request.call_args.args
    assert sent_data == {"method": "anyMethod", "key": "value", "num": 7}


# get_fragment_hash Referer tests


@pytest.mark.asyncio
@pytest.mark.parametrize("page_url", ["https://fragment.com", "https://fragment.com/"])
async def test_get_fragment_hash_root_url_uses_origin_as_referer(page_url: str) -> None:
    response = MagicMock(spec=Response)
    response.status_code = 200
    response.text = "/api?hash=abc123"

    session = AsyncMock(spec=AsyncSession)
    session.get = AsyncMock(return_value=response)

    await get_fragment_hash(session, {}, page_url)

    request_headers = session.get.call_args.kwargs["headers"]
    assert request_headers["referer"] == "https://fragment.com"


@pytest.mark.asyncio
async def test_get_fragment_hash_path_url_uses_parent_as_referer() -> None:
    response = MagicMock(spec=Response)
    response.status_code = 200
    response.text = "/api?hash=abc123"

    session = AsyncMock(spec=AsyncSession)
    session.get = AsyncMock(return_value=response)

    await get_fragment_hash(session, {}, "https://fragment.com/stars/buy")

    request_headers = session.get.call_args.kwargs["headers"]
    assert request_headers["referer"] == "https://fragment.com/stars"


# fragment_request HTTP status tests


@pytest.mark.asyncio
async def test_fragment_request_non_200_raises() -> None:
    response = MagicMock(spec=Response)
    response.status_code = 429

    session = AsyncMock(spec=AsyncSession)
    session.post = AsyncMock(return_value=response)

    with pytest.raises(FragmentPageError, match="429"):
        await fragment_request(session, FAKE_HASH, {}, {"method": "anyMethod"})
