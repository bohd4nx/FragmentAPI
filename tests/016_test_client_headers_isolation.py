from pyfragment import FragmentClient
from pyfragment.core.constants import BASE_HEADERS
from tests.shared import VALID_API_KEY, VALID_COOKIES, VALID_SEED


def test_default_headers_are_not_shared_between_clients() -> None:
    client_a = FragmentClient(seed=VALID_SEED, api_key=VALID_API_KEY, cookies=VALID_COOKIES)
    client_b = FragmentClient(seed=VALID_SEED, api_key=VALID_API_KEY, cookies=VALID_COOKIES)

    client_a.headers["X-Test"] = "client-a"

    assert client_a.headers is not client_b.headers
    assert client_a.headers is not BASE_HEADERS
    assert client_b.headers["X-Test"] != "client-a"
    assert "X-Test" not in BASE_HEADERS


def test_custom_headers_are_copied_at_client_creation() -> None:
    source_headers = {"X-Test": "source"}
    client = FragmentClient(
        seed=VALID_SEED,
        api_key=VALID_API_KEY,
        cookies=VALID_COOKIES,
        headers=source_headers,
    )

    source_headers["X-Test"] = "changed-source"
    client.headers["X-Client"] = "client-only"

    assert client.headers["X-Test"] == "source"
    assert client.headers["X-Client"] == "client-only"
    assert "X-Client" not in source_headers
