from tap_drip.streams.abstracts import FullTableStream

class Conversions(FullTableStream):
    tap_stream_id = "conversions"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "goals"
    path = "{account_id}/goals"
    parent = "accounts"
