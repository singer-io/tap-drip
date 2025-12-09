from tap_drip.streams.abstracts import ChildFullTableStream

class Forms(ChildFullTableStream):
    tap_stream_id = "forms"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "forms"
    path = "{}/forms"
    parent = "accounts"
