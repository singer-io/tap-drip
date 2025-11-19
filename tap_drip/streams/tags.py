from tap_drip.streams.abstracts import FullTableStream

class Tags(FullTableStream):
    tap_stream_id = "tags"
    key_properties = ["tag_name", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "tags"
    path = "{account_id}/tags"
    parent = "accounts"
