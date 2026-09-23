from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any
import json

@dataclass
class ActionReceipt:
    action: str
    target: str
    success: bool
    before_state: str = "unknown"
    after_state: str = "unknown"
    detail: dict[str, Any] | None = None
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)
