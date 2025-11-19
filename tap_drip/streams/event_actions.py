from tap_drip.streams.abstracts import FullTableStream

class EventActions(FullTableStream):
    tap_stream_id = "event_actions"
    key_properties = ["event_action", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "event_actions"
    path = "{account_id}/event_actions"
    parent = "accounts"
