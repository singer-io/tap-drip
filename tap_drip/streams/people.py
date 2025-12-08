from tap_drip.streams.abstracts import ChildFullTableStream

class People(ChildFullTableStream):
    tap_stream_id = "people"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "subscribers"
    path = "{}/subscribers"
    parent = "accounts"

    def update_params(self, **kwargs):
        """
        This method overrides the parent class's update_params method to specifically
        filter for subscribers with an 'all' status.
        """
        kwargs["status"] = "all"
        return super().update_params(**kwargs)
