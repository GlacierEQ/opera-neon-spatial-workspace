"""Test suite for Opera Neon Spatial Workspace solution."""
import unittest
from opera_neon_spatial_workspace import OperaNeonSpatialWorkspace

class TestOperaNeonSpatialWorkspace(unittest.TestCase):

    def test_spatial_tab_addition(self):
        workspace = OperaNeonSpatialWorkspace()
        res = workspace.add_spatial_tab("News", "https://news.ycombinator.com", 100.0, 200.0)
        
        self.assertEqual(res["status"], "NEON_SPATIAL_ACTIVE")
        self.assertEqual(res["active_tabs"], 1)

if __name__ == "__main__":
    unittest.main()
