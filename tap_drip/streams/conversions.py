from tap_drip.streams.abstracts import ChildFullTableStream

class Conversions(ChildFullTableStream):
    tap_stream_id = "conversions"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "goals"
    path = "{}/goals"
    parent = "accounts"
