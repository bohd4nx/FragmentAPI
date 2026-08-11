from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PremiumResult:
    transaction_id: str
    username: str
    amount: int
    confirmed: bool = False

    def __repr__(self) -> str:
        return (
            f"PremiumResult(username='{self.username}', amount={self.amount} months, "
            f"tx='{self.transaction_id}', confirmed={self.confirmed})"
        )


@dataclass
class StarsResult:
    transaction_id: str
    username: str
    amount: int
    confirmed: bool = False

    def __repr__(self) -> str:
        return (
            f"StarsResult(username='{self.username}', amount={self.amount} stars, "
            f"tx='{self.transaction_id}', confirmed={self.confirmed})"
        )
