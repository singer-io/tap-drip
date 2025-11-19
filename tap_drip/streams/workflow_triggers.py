from tap_drip.streams.abstracts import FullTableStream

class WorkflowTriggers(FullTableStream):
    tap_stream_id = "workflow_triggers"
    key_properties = ["id", "account_id", "workflow_id"]
    replication_method = "FULL_TABLE"
    data_key = "triggers"
    path = "{account_id}/workflows/{workflow_id}/triggers"
    parent = "workflows"
