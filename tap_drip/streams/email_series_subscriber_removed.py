from tap_drip.streams.abstracts import ChildFullTableStream

class EmailSeriesSubscriberRemoved(ChildFullTableStream):
    tap_stream_id = "email_series_subscriber_removed"
    key_properties = ["id", "account_id", "campaign_id"]
    replication_method = "FULL_TABLE"
    data_key = "subscribers"
    path = "{}/campaigns/{}/subscribers"
    parent = "email_series_campaigns"

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child streams with account_id and campaign_id."""
        if parent_obj:
            return f"{self.client.base_url}/{self.path.format(parent_obj.get('account_id'), parent_obj.get('id'))}"
        return f"{self.client.base_url}/{self.path}"

    def modify_object(self, record, parent_record=None):
        """Add account_id and campaign_id from parent to the record."""
        if parent_record:
            record['account_id'] = parent_record.get('account_id')
            record['campaign_id'] = parent_record.get('id')
        return record

    def update_params(self, **kwargs):
        """
        This method overrides the parent class's update_params method to specifically
        filter for subscribers with an 'removed' status.
        """
        kwargs["status"] = "removed"
        return super().update_params(**kwargs)
