from tap_drip.streams.abstracts import FullTableStream

class Accounts(FullTableStream):
    tap_stream_id = "accounts"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "accounts"
    path = "accounts"
    children = [
        'conversions',
        'custom_field_identifiers',
        'email_series_campaigns',
        'event_actions',
        'forms',
        'single_email_campaigns',
        'people',
        'tags',
        'workflows'
    ]
