from tap_drip.streams.accounts import Accounts
from tap_drip.streams.conversions import Conversions
from tap_drip.streams.custom_field_identifiers import CustomFieldIdentifiers
from tap_drip.streams.email_series_campaigns import EmailSeriesCampaigns
from tap_drip.streams.email_series_subscriber_active import EmailSeriesSubscriberActive
from tap_drip.streams.email_series_subscriber_removed import EmailSeriesSubscriberRemoved
from tap_drip.streams.email_series_subscriber_unsubscribed import EmailSeriesSubscriberUnsubscribed
from tap_drip.streams.event_actions import EventActions
from tap_drip.streams.forms import Forms
from tap_drip.streams.single_email_campaigns import SingleEmailCampaigns
from tap_drip.streams.people import People
from tap_drip.streams.tags import Tags
from tap_drip.streams.users import Users
from tap_drip.streams.workflows import Workflows
from tap_drip.streams.workflow_triggers import WorkflowTriggers

STREAMS = {
    "accounts": Accounts,
    "conversions": Conversions,
    "custom_field_identifiers": CustomFieldIdentifiers,
    "email_series_campaigns": EmailSeriesCampaigns,
    "email_series_subscriber_active": EmailSeriesSubscriberActive,
    "email_series_subscriber_removed": EmailSeriesSubscriberRemoved,
    "email_series_subscriber_unsubscribed": EmailSeriesSubscriberUnsubscribed,
    "event_actions": EventActions,
    "forms": Forms,
    "single_email_campaigns": SingleEmailCampaigns,
    "people": People,
    "tags": Tags,
    "users": Users,
    "workflows": Workflows,
    "workflow_triggers": WorkflowTriggers
}
