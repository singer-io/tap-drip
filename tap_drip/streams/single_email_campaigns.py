from tap_drip.streams.abstracts import FullTableStream

class SingleEmailCampaigns(FullTableStream):
    tap_stream_id = "single_email_campaigns"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "broadcasts"
    path = "{account_id}/broadcasts"
    parent = "accounts"
