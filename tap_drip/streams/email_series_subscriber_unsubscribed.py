from tap_drip.streams.abstracts import FullTableStream

class EmailSeriesSubscriberUnsubscribed(FullTableStream):
    tap_stream_id = "email_series_subscriber_unsubscribed"
    key_properties = ["id", "account_id", "campaign_id"]
    replication_method = "FULL_TABLE"
    data_key = "subscribers"
    path = "{account_id}/campaigns/{campaign_id}/subscribers"
    parent = "email_series_campaigns"
