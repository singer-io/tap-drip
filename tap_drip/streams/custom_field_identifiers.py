from tap_drip.streams.abstracts import FullTableStream

class CustomFieldIdentifiers(FullTableStream):
    tap_stream_id = "custom_field_identifiers"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "custom_field_identifiers"
    path = "{account_id}/custom_field_identifiers"
    parent = "accounts"
