from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from pyfragment.domains.purchases.purchase import purchase_premium, purchase_stars
from pyfragment.enums import PaymentMethod
from pyfragment.exceptions import ConfigurationError

UNSUPPORTED_PAYMENT_METHODS = (
    PaymentMethod.USDT_ETH,
    PaymentMethod.USDT_POL,
    PaymentMethod.USDC_ETH,
    PaymentMethod.USDC_BASE,
    PaymentMethod.USDC_POL,
)


@pytest.mark.asyncio
@pytest.mark.parametrize("payment_method", UNSUPPORTED_PAYMENT_METHODS)
async def test_purchase_stars_rejects_unsupported_payment_method_before_api_call(
    payment_method: PaymentMethod,
) -> None:
    client = MagicMock()
    client.call = AsyncMock(
        side_effect=[
            {"found": {"recipient": "recipient"}},
            {},
            {"req_id": "request", "amount": "1"},
            {"need_verify": False},
        ]
    )

    with (
        patch("pyfragment.domains.purchases.purchase.get_account_info", AsyncMock(return_value={})),
        patch("pyfragment.domains.purchases.purchase.process_transaction", AsyncMock(return_value="tx")),
        pytest.raises(ConfigurationError),
    ):
        await purchase_stars(client, "@user", amount=500, payment_method=payment_method)

    client.call.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("payment_method", UNSUPPORTED_PAYMENT_METHODS)
async def test_purchase_premium_rejects_unsupported_payment_method_before_api_call(
    payment_method: PaymentMethod,
) -> None:
    client = MagicMock()
    client.call = AsyncMock(
        side_effect=[
            {"found": {"recipient": "recipient"}},
            {},
            {"req_id": "request", "amount": "1"},
            {"need_verify": False},
        ]
    )

    with (
        patch("pyfragment.domains.purchases.purchase.get_account_info", AsyncMock(return_value={})),
        patch("pyfragment.domains.purchases.purchase.process_transaction", AsyncMock(return_value="tx")),
        pytest.raises(ConfigurationError),
    ):
        await purchase_premium(client, "@user", months=3, payment_method=payment_method)

    client.call.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("payment_method", (PaymentMethod.GRAM, PaymentMethod.USDT_GRAM))
async def test_supported_payment_methods_remain_accepted(payment_method: PaymentMethod) -> None:
    client = MagicMock()
    client.call = AsyncMock(
        side_effect=[
            {"found": {"recipient": "recipient"}},
            {},
            {"req_id": "request", "amount": "1"},
            {"need_verify": False},
        ]
    )

    with (
        patch("pyfragment.domains.purchases.purchase.get_account_info", AsyncMock(return_value={})),
        patch("pyfragment.domains.purchases.purchase.process_transaction", AsyncMock(return_value="tx")),
    ):
        result = await purchase_stars(client, "@user", amount=500, payment_method=payment_method)

    assert result.transaction_id == "tx"
    init_request = client.call.await_args_list[2]
    assert init_request.args[0] == "initBuyStarsRequest"
    assert init_request.args[1]["payment_method"] == payment_method
