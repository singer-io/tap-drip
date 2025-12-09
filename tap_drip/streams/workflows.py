from tap_drip.streams.abstracts import ChildFullTableStream

class Workflows(ChildFullTableStream):
    tap_stream_id = "workflows"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "workflows"
    path = "{}/workflows"
    parent = "accounts"
    children = ['workflow_triggers']
