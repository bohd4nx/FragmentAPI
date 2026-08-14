"""Parse Fragment init responses to the payment amount the transaction should cover."""

from pyfragment.domains.payments import parse_required_payment_amount


def test_parse_required_payment_amount_ton_uses_amount() -> None:
    init_response = {"amount": "0.326"}
    assert parse_required_payment_amount(init_response) == 0.326


def test_parse_required_payment_amount_usdt_uses_amount() -> None:
    init_response = {
        "amount": "0.00075",
        "content": '<span class="icon-before icon-usd">0.75</span>',
    }
    assert parse_required_payment_amount(init_response) == 0.00075


def test_parse_required_payment_amount_usdt_falls_back_to_amount() -> None:
    init_response = {"amount": "1.25", "content": "<p>no usd icon</p>"}
    assert parse_required_payment_amount(init_response) == 1.25


def test_parse_required_payment_amount_strips_thousand_separators() -> None:
    init_response = {"amount": "1,000,000,000"}
    assert parse_required_payment_amount(init_response) == 1_000_000_000.0
