from tap_drip.streams.abstracts import ChildFullTableStream

class SingleEmailCampaigns(ChildFullTableStream):
    tap_stream_id = "single_email_campaigns"
    key_properties = ["id", "account_id"]
    replication_method = "FULL_TABLE"
    data_key = "broadcasts"
    path = "{}/broadcasts"
    parent = "accounts"
