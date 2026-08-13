import pytest

from pyfragment.exceptions import WalletError
from pyfragment.services.tonapi.account import check_gram_payment_balance


@pytest.mark.asyncio
async def test_payment_amount_alone_is_not_sufficient_for_gram_transfer() -> None:
    with pytest.raises(WalletError, match="required"):
        await check_gram_payment_balance(
            balance_gram=0.5,
            amount_gram=0.5,
            required_payment_amount=None,
        )


@pytest.mark.asyncio
async def test_balance_must_include_full_gram_fee_reserve() -> None:
    with pytest.raises(WalletError, match="required"):
        await check_gram_payment_balance(
            balance_gram=0.829999999,
            amount_gram=0.5,
            required_payment_amount=None,
        )

    await check_gram_payment_balance(
        balance_gram=0.83,
        amount_gram=0.5,
        required_payment_amount=None,
    )


@pytest.mark.asyncio
async def test_required_payment_amount_is_also_covered_by_fee_reserve() -> None:
    with pytest.raises(WalletError, match="required"):
        await check_gram_payment_balance(
            balance_gram=1.079999999,
            amount_gram=0.5,
            required_payment_amount=0.75,
        )

    await check_gram_payment_balance(
        balance_gram=1.08,
        amount_gram=0.5,
        required_payment_amount=0.75,
    )
