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
            'accounts',
            'conversions',
            'email_series_subscriber_active',
            'email_series_subscriber_removed',
            'email_series_subscriber_unsubscribed',
            'event_actions',
            'forms',
            'people',
            'users',
        }
        return self.expected_stream_names().difference(streams_to_exclude)
