"""PsychoRadar CALL: local campaign safeguards (no external ad changes)."""
from dataclasses import dataclass

@dataclass(frozen=True)
class CampaignSnapshot:
    spend_pln: float
    monthly_limit_pln: float
    tracked_calls: int

def evaluate(snapshot: CampaignSnapshot) -> dict:
    if snapshot.monthly_limit_pln <= 0 or snapshot.spend_pln < 0:
        raise ValueError("Invalid budget")
    return {
        "budget_exceeded": snapshot.spend_pln >= snapshot.monthly_limit_pln,
        "remaining_pln": max(0.0, snapshot.monthly_limit_pln - snapshot.spend_pln),
        "cost_per_call_pln": round(snapshot.spend_pln / snapshot.tracked_calls, 2)
            if snapshot.tracked_calls > 0 else None,
        "action": "REVIEW_PAUSE" if snapshot.spend_pln >= snapshot.monthly_limit_pln else "MONITOR",
    }
