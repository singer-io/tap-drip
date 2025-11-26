from tap_drip.streams.abstracts import ChildFullTableStream

class CustomFieldIdentifiers(ChildFullTableStream):
    tap_stream_id = "custom_field_identifiers"
    key_properties = ["custom_field_id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "custom_field_identifiers"
    path = "{}/custom_field_identifiers"
    parent = "accounts"

    def modify_object(self, record, parent_record = None):
        """Handle cases where record is a string instead of a dict."""
        if isinstance(record, str):
            obj = record
            record = {
                "custom_field_id": obj
            }
        return super().modify_object(record, parent_record)
