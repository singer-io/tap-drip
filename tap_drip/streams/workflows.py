from tap_drip.streams.abstracts import FullTableStream

class Workflows(FullTableStream):
    tap_stream_id = "workflows"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "workflows"
    path = "{account_id}/workflows"
    parent = "accounts"
    children = ['workflow_triggers']
