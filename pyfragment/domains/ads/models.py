from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AdsTopupResult:
    transaction_id: str
    username: str
    amount: int
    confirmed: bool = False

    def __repr__(self) -> str:
        return (
            f"AdsTopupResult(username='{self.username}', amount={self.amount} GRAM (ex TON), "
            f"tx='{self.transaction_id}', confirmed={self.confirmed})"
        )


@dataclass
class AdsRechargeResult:
    transaction_id: str
    amount: int
    confirmed: bool = False

    def __repr__(self) -> str:
        return f"AdsRechargeResult(amount={self.amount} GRAM (ex TON), tx='{self.transaction_id}', confirmed={self.confirmed})"
