from base import dripBaseTest


class dripStartDateTest(dripBaseTest):
    """Instantiate start date according to the desired data set and run the test.

    Note: All streams are FULL_TABLE with no replication keys.
    StartDateTest requires streams with replication keys.
    """

    @staticmethod
    def name():
        return "tap_tester_drip_start_date_test"

    def streams_to_test(self):
        # Due to test data not present excluding streams
        streams_to_exclude = {}
        return self.expected_stream_names().difference(streams_to_exclude)

    @property
    def start_date_1(self):
        return "2015-03-25T00:00:00Z"

    @property
    def start_date_2(self):
        return "2017-01-25T00:00:00Z"
