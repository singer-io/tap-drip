from tap_tester.base_suite_tests.pagination_test import PaginationTest
from base import dripBaseTest

class dripPaginationTest(PaginationTest, dripBaseTest):
    """
    Ensure tap can replicate multiple pages of data for streams that use pagination.
    """

    @staticmethod
    def name():
        return "tap_tester_drip_pagination_test"

    def streams_to_test(self):
        # Exclude streams that don't have enough data to test pagination
        streams_to_exclude = {
            "conversions",
            "accounts",
            "users",
            "email_series_subscriber_removed"
        }
        return self.expected_stream_names().difference(streams_to_exclude)
