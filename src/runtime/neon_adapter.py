"""Opera Neon connector adapter boundary."""

from dataclasses import dataclass
from typing import Any, Protocol

class NeonTransport(Protocol):
    def call(self, action: str, **kwargs: Any) -> Any: ...

@dataclass
class NeonAdapter:
    transport: NeonTransport

    def health(self):
        return {"connected": True, "adapter": "opera-neon"}

    def inspect(self, target):
        return self.transport.call("inspect", target=target)

    def click(self, target):
        return self.transport.call("click", target=target)

    def fill(self, target, value):
        return self.transport.call("fill", target=target, value=value)

    def screenshot(self):
        return self.transport.call("screenshot")
