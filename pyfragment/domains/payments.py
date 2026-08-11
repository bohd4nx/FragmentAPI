from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pyfragment.client import FragmentClient

logger = logging.getLogger(__name__)


def parse_required_payment_amount(init_response: dict[str, Any]) -> float | None:
    raw_amount = init_response.get("amount")
    try:
        return float(str(raw_amount))
    except (TypeError, ValueError):
        return None


async def cancel_invoice(client: FragmentClient, req_id: str, page_url: str) -> None:
    try:
        await client.call("cancelInvoice", {"req_id": req_id}, page_url=page_url)
    except Exception:
        logger.exception("Failed to cancel Fragment invoice '%s'", req_id)
