"""ADZO Social Publisher: local draft workflow. Does not post or store passwords."""
from dataclasses import dataclass, field
from datetime import datetime

SUPPORTED = {"facebook_page", "instagram_professional", "google_business_profile"}

@dataclass
class Draft:
    text: str
    media_paths: list[str] = field(default_factory=list)
    targets: list[str] = field(default_factory=list)
    publish_at: datetime | None = None

def prepare(draft: Draft) -> dict:
    if not draft.text.strip() and not draft.media_paths:
        raise ValueError("Add text or media")
    unknown = set(draft.targets) - SUPPORTED
    if unknown:
        raise ValueError(f"Unsupported targets: {sorted(unknown)}")
    if not draft.targets:
        raise ValueError("Choose at least one target")
    return {"status": "awaiting_approval", "targets": draft.targets,
            "scheduled": draft.publish_at is not None,
            "requires_platform_authorization": True}
