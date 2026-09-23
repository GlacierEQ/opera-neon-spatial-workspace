from .receipts import ActionReceipt


class NeonRuntime:
    """Verification-first wrapper for browser execution adapters.

    This layer intentionally separates intent, execution, and verification so
    browser actions can produce durable receipts instead of silent clicks.
    """

    def __init__(self, adapter=None):
        self.adapter = adapter

    def health(self):
        return {
            "adapter_connected": self.adapter is not None,
            "runtime": "opera-neon-execution-runtime",
        }

    def inspect(self):
        if not self.adapter:
            return None
        return self.adapter.inspect()

    def execute(self, action, target, **kwargs):
        before = kwargs.pop("before_state", None)
        try:
            result = getattr(self.adapter, action)(**kwargs) if self.adapter else None
            return ActionReceipt(
                action=action,
                target=target,
                success=True,
                before_state=before,
                after_state=kwargs.get("after_state"),
                detail=result,
            )
        except Exception as exc:
            return ActionReceipt(
                action=action,
                target=target,
                success=False,
                before_state=before,
                detail={"error": str(exc)},
            )
