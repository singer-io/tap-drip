from tap_drip.streams.abstracts import ChildFullTableStream

class EventActions(ChildFullTableStream):
    tap_stream_id = "event_actions"
    key_properties = ["event_action", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "event_actions"
    path = "{}/event_actions"
    parent = "accounts"

    def modify_object(self, record, parent_record = None):
        """Handle cases where record is a string instead of a dict."""
        if isinstance(record, str):
            obj = record
            record = {
                "event_action": obj
            }
        return super().modify_object(record, parent_record)
