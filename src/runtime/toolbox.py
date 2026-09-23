"""Unified Opera Neon execution toolbox."""

class ExecutionToolbox:
    def __init__(self, neon):
        self.neon = neon

    def inspect(self, target):
        return self.neon.inspect(target)

    def click(self, target):
        return self.neon.click(target)

    def fill(self, target, value):
        return self.neon.fill(target, value)

    def screenshot(self):
        return self.neon.screenshot()
