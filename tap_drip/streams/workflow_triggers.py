from tap_drip.streams.abstracts import ChildFullTableStream

class WorkflowTriggers(ChildFullTableStream):
    tap_stream_id = "workflow_triggers"
    key_properties = ["id", "account_id", "workflow_id"]
    replication_method = "FULL_TABLE"
    data_key = "triggers"
    path = "{}/workflows/{}/triggers"
    parent = "workflows"

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child streams with account_id and workflow_id."""
        if parent_obj:
            return f"{self.client.base_url}/{self.path.format(parent_obj.get('account_id'), parent_obj.get('id'))}"
        return f"{self.client.base_url}/{self.path}"

    def modify_object(self, record, parent_record=None):
        """Add account_id and workflow_id from parent to the record."""
        if parent_record:
            record['account_id'] = parent_record.get('account_id')
            record['workflow_id'] = parent_record.get('id')
        return record
