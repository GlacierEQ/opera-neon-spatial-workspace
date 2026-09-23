from .receipts import ActionReceipt

class NeonRuntime:
    """Execution wrapper for Opera Neon actions.

    The runtime intentionally separates action execution from verification so
    every browser mutation can produce a durable receipt.
    """

    def __init__(self, adapter=None):
        self.adapter = adapter
        self.receipts = []

    def health(self):
        if self.adapter and hasattr(self.adapter, "health"):
            return self.adapter.health()
        return {"connected": False, "reason": "adapter_not_attached"}

    def execute(self, action, target, **kwargs):
        before = self.inspect_state(target)
        try:
            result = self.adapter.execute(action, target, **kwargs) if self.adapter else None
            after = self.inspect_state(target)
            receipt = ActionReceipt(action, target, True, before, after, {"result": result})
        except Exception as exc:
            receipt = ActionReceipt(action, target, False, before, before, {"error": str(exc)})
        self.receipts.append(receipt)
        return receipt

    def inspect_state(self, target):
        if self.adapter and hasattr(self.adapter, "inspect"):
            return self.adapter.inspect(target)
        return "unverified"
