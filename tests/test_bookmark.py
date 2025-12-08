from base import dripBaseTest
from tap_tester.base_suite_tests.bookmark_test import BookmarkTest


class dripBookMarkTest(BookmarkTest, dripBaseTest):
    """Test tap sets a bookmark and respects it for the next sync of a
    stream."""
    bookmark_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    initial_bookmarks = {
        "bookmarks": {
        }
    }
    @staticmethod
    def name():
        return "tap_tester_drip_bookmark_test"

    def streams_to_test(self):
        # Due to test data not present excluding streams
        streams_to_exclude = {
            "email_series_subscriber_unsubscribed",
            "conversions"
        }
        return self.expected_stream_names().difference(streams_to_exclude)
