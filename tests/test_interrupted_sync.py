
import unittest
from base import dripBaseTest


class dripInterruptedSyncTest(dripBaseTest):
    """Test tap recovers from an interrupted sync.

    NOTE: This test is skipped because all streams in tap-drip use FULL_TABLE
    replication method. Interrupted sync tests rely on bookmarks which only
    apply to INCREMENTAL streams.
    """

    @staticmethod
    def name():
        return "tap_tester_drip_interrupted_sync_test"

    @unittest.skip("All streams use FULL_TABLE replication - interrupted sync test not applicable")
    def test_run(self):
        """Skipped - no incremental streams in tap-drip"""
        pass
