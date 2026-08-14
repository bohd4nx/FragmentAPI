from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StarsGiveawayResult:
    transaction_id: str
    channel: str
    winners: int
    amount: int
    confirmed: bool = False

    def __repr__(self) -> str:
        return (
            f"StarsGiveawayResult(channel='{self.channel}', winners={self.winners}, "
            f"amount={self.amount} stars per winner, tx='{self.transaction_id}', confirmed={self.confirmed})"
        )


@dataclass
class PremiumGiveawayResult:
    transaction_id: str
    channel: str
    winners: int
    amount: int
    confirmed: bool = False

    def __repr__(self) -> str:
        return (
            f"PremiumGiveawayResult(channel='{self.channel}', winners={self.winners}, "
            f"amount={self.amount} months per winner, tx='{self.transaction_id}', confirmed={self.confirmed})"
        )
