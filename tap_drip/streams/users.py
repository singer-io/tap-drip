from tap_drip.streams.abstracts import FullTableStream

class Users(FullTableStream):
    tap_stream_id = "users"
    key_properties = ["email"]
    replication_method = "FULL_TABLE"
    data_key = "users"
    path = "user"
