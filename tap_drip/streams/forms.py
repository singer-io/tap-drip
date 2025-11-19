from tap_drip.streams.abstracts import FullTableStream

class Forms(FullTableStream):
    tap_stream_id = "forms"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "forms"
    path = "{account_id}/forms"
    parent = "accounts"
