from tap_drip.streams.abstracts import ChildFullTableStream

class Tags(ChildFullTableStream):
    tap_stream_id = "tags"
    key_properties = ["tag_id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "tags"
    path = "{}/tags"
    parent = "accounts"

    def modify_object(self, record, parent_record = None):
        """Handle cases where record is a string instead of a dict."""
        if isinstance(record, str):
            obj = record
            record = {
                "tag_id": obj
            }
        return super().modify_object(record, parent_record)