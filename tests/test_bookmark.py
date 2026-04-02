import unittest
from base import dripBaseTest


class dripBookMarkTest(dripBaseTest):
    """Test tap sets a bookmark and respects it for the next sync of a stream.

    NOTE: This test is skipped because all streams in tap-drip use FULL_TABLE
    replication method. Bookmark tests only apply to INCREMENTAL streams.
    """

    @staticmethod
    def name():
        return "tap_tester_drip_bookmark_test"

    @unittest.skip("All streams use FULL_TABLE replication - bookmark test not applicable")
    def test_run(self):
        """Skipped - no incremental streams in tap-drip"""
        pass
