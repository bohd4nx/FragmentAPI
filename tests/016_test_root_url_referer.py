from unittest.mock import AsyncMock, MagicMock

import pytest
from curl_cffi.requests import AsyncSession, Response

from pyfragment.core.transport import get_fragment_hash


@pytest.mark.asyncio
@pytest.mark.parametrize("page_url", ["https://fragment.com", "https://fragment.com/"])
async def test_root_page_uses_origin_as_referer(page_url: str) -> None:
    response = MagicMock(spec=Response)
    response.status_code = 200
    response.text = "/api?hash=abc123"

    session = AsyncMock(spec=AsyncSession)
    session.get = AsyncMock(return_value=response)

    assert await get_fragment_hash(session, {}, page_url) == "abc123"

    request_headers = session.get.call_args.kwargs["headers"]
    assert request_headers["referer"] == "https://fragment.com"


@pytest.mark.asyncio
async def test_nested_page_uses_immediate_parent_as_referer() -> None:
    response = MagicMock(spec=Response)
    response.status_code = 200
    response.text = "/api?hash=abc123"

    session = AsyncMock(spec=AsyncSession)
    session.get = AsyncMock(return_value=response)

    assert await get_fragment_hash(session, {}, "https://fragment.com/stars/buy") == "abc123"

    request_headers = session.get.call_args.kwargs["headers"]
    assert request_headers["referer"] == "https://fragment.com/stars"
