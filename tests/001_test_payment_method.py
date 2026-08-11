from unittest.mock import AsyncMock, MagicMock

import pytest

from pyfragment.domains.purchases.purchase import purchase_stars
from pyfragment.enums import PaymentMethod
from pyfragment.exceptions import ConfigurationError


@pytest.mark.asyncio
async def test_purchase_stars_rejects_unsupported_payment_method() -> None:
    client = MagicMock()
    client.call = AsyncMock()

    with pytest.raises(ConfigurationError):
        await purchase_stars(
            client,
            "@user",
            amount=500,
            payment_method=PaymentMethod.USDT_ETH,
        )

    client.call.assert_not_awaited()
