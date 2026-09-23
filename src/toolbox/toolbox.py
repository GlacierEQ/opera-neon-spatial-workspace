from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable


@dataclass
class ToolReceipt:
    tool: str
    success: bool
    detail: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class OperaNeonToolbox:
    def __init__(self, adapter: Any = None):
        self.adapter = adapter
        self.receipts: list[ToolReceipt] = []

    def run(self, tool: str, action: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        try:
            result = action(*args, **kwargs)
            self.receipts.append(ToolReceipt(tool, True, {"result": str(result)}))
            return result
        except Exception as exc:
            self.receipts.append(ToolReceipt(tool, False, {"error": str(exc)}))
            raise

    def latest_receipts(self) -> list[ToolReceipt]:
        return self.receipts[-50:]
