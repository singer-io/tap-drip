from tap_drip.streams.abstracts import FullTableStream

class EmailSeriesCampaigns(FullTableStream):
    tap_stream_id = "email_series_campaigns"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "campaigns"
    path = "{account_id}/campaigns"
    parent = "accounts"
    children = [
        'email_series_subscriber_active',
        'email_series_subscriber_removed',
        'email_series_subscriber_unsubscribed'
    ]
