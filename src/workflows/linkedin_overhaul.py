"""Verified LinkedIn overhaul workflow."""

class LinkedInOverhaul:
    STEPS = [
        "inspect_profile",
        "open_intro_edit",
        "replace_headline",
        "verify_headline",
        "replace_about",
        "verify_about",
        "replace_experience",
        "verify_experience",
    ]

    def __init__(self, runtime):
        self.runtime = runtime

    def plan(self):
        return self.STEPS

    def run(self):
        return [self.runtime.execute(step, {}) for step in self.STEPS]
