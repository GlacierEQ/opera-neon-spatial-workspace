from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass
class ActionReceipt:
    action: str
    target: str
    success: bool
    before_state: str | None = None
    after_state: str | None = None
    detail: Any = None
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        return asdict(self)
