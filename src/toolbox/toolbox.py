from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Receipt:
    action: str
    target: str
    ok: bool
    detail: dict = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class NeonToolbox:
    """Execution primitives for browser automation workflows.

    Adapter-independent until bound to a live Neon connector.
    """
    def __init__(self, adapter=None):
        self.adapter = adapter
        self.receipts = []

    def inspect(self):
        return self._run("inspect", "page")

    def navigate(self, url):
        return self._run("navigate", url)

    def find(self, target):
        return self._run("find", target)

    def click(self, target):
        return self._run("click", target)

    def fill(self, target, value):
        return self._run("fill", target, {"value": value})

    def verify(self, expected):
        return self._run("verify", expected)

    def recover(self):
        return self._run("recover", "session")

    def _run(self, action, target, detail=None):
        ok = self.adapter is not None
        receipt = Receipt(action, target, ok, detail or {})
        self.receipts.append(receipt)
        return receipt
