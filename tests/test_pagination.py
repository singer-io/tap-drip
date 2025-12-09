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
        # Due to test data not present excluding streams
        streams_to_exclude = {
            "email_series_subscriber_unsubscribed",
            "conversions"
        }
        return self.expected_stream_names().difference(streams_to_exclude)
