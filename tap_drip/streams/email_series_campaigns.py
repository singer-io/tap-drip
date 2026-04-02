from tap_drip.streams.abstracts import ChildFullTableStream

class EmailSeriesCampaigns(ChildFullTableStream):
    tap_stream_id = "email_series_campaigns"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "campaigns"
    path = "{}/campaigns"
    parent = "accounts"
    children = [
        'email_series_subscriber_active',
        'email_series_subscriber_removed',
        'email_series_subscriber_unsubscribed'
    ]
