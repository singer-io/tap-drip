from tap_drip.streams.abstracts import FullTableStream

class Peoples(FullTableStream):
    tap_stream_id = "peoples"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "subscribers"
    path = "{account_id}/subscribers"
    parent = "accounts"
