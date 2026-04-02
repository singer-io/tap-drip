# tap-drip

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md).

This tap:

- Pulls raw data from the [drip API].
- Extracts the following resources:
    - [Accounts](https://developer.drip.com/?shell#list-all-accounts)

    - [Conversions](https://developer.drip.com/?shell#list-all-conversions)

    - [CustomFieldIdentifiers](https://developer.drip.com/?shell#list-all-custom-field-identifiers-used-in-an-account)

    - [EmailSeriesCampaigns](https://developer.drip.com/?shell#list-all-email-series-campaigns)

    - [EmailSeriesSubscriberActive](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign)

    - [EmailSeriesSubscriberRemoved](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign)

    - [EmailSeriesSubscriberUnsubscribed](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign)

    - [EventActions](https://developer.drip.com/?shell#list-all-custom-events-actions-used-in-an-account)

    - [Forms](https://developer.drip.com/?shell#list-all-forms)

    - [People](https://developer.drip.com/?shell#list-all-subscribers)

    - [SingleEmailCampaigns](https://developer.drip.com/?shell#list-all-single-email-campaigns)

    - [Tags](https://developer.drip.com/?shell#list-all-tags-used-in-an-account)

    - [Users](https://developer.drip.com/?shell#users)

    - [Workflows](https://developer.drip.com/?shell#list-all-workflows)

    - [WorkflowTriggers](https://developer.drip.com/?shell#list-all-workflow-triggers)

- Outputs the schema for each resource
- Incrementally pulls data based on the input state


## Streams


**[accounts](https://developer.drip.com/?shell#list-all-accounts)**
- Data Key = accounts
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[conversions](https://developer.drip.com/?shell#list-all-conversions)**
- Data Key = goals
- Primary keys: ['id', 'account_id']
- Replication strategy: FULL_TABLE

**[custom_field_identifiers](https://developer.drip.com/?shell#list-all-custom-field-identifiers-used-in-an-account)**
- Data Key = custom_field_identifiers
- Primary keys: ['custom_field_id', 'account_id']
- Replication strategy: FULL_TABLE

**[email_series_campaigns](https://developer.drip.com/?shell#list-all-email-series-campaigns)**
- Data Key = campaigns
- Primary keys: ['id', 'account_id']
- Replication strategy: FULL_TABLE

**[email_series_subscriber_active](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign)**
- Data Key = subscribers
- Primary keys: ['id', 'account_id', 'campaign_id']
- Replication strategy: FULL_TABLE

**[email_series_subscriber_removed](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign)**
- Data Key = subscribers
- Primary keys: ['id', 'account_id', 'campaign_id']
- Replication strategy: FULL_TABLE

**[email_series_subscriber_unsubscribed](https://developer.drip.com/?shell#list-all-subscribers-subscribed-to-an-email-series-campaign)**
- Data Key = subscribers
- Primary keys: ['id', 'account_id', 'campaign_id']
- Replication strategy: FULL_TABLE

**[event_actions](https://developer.drip.com/?shell#list-all-custom-events-actions-used-in-an-account)**
- Data Key = event_actions
- Primary keys: ['event_action', 'account_id']
- Replication strategy: FULL_TABLE

**[forms](https://developer.drip.com/?shell#list-all-forms)**
- Data Key = forms
- Primary keys: ['id', 'account_id']
- Replication strategy: FULL_TABLE

**[people](https://developer.drip.com/?shell#list-all-subscribers)**
- Data Key = subscribers
- Primary keys: ['id', 'account_id']
- Replication strategy: FULL_TABLE

**[single_email_campaigns](https://developer.drip.com/?shell#list-all-single-email-campaigns)**
- Data Key = broadcasts
- Primary keys: ['id', 'account_id']
- Replication strategy: FULL_TABLE

**[tags](https://developer.drip.com/?shell#list-all-tags-used-in-an-account)**
- Data Key = tags
- Primary keys: ['tag_id', 'account_id']
- Replication strategy: FULL_TABLE

**[users](https://developer.drip.com/?shell#users)**
- Data Key = users
- Primary keys: ['email']
- Replication strategy: FULL_TABLE

**[workflows](https://developer.drip.com/?shell#list-all-workflows)**
- Data Key = workflows
- Primary keys: ['id', 'account_id']
- Replication strategy: FULL_TABLE

**[workflow_triggers](https://developer.drip.com/?shell#list-all-workflow-triggers)**
- Data Key = triggers
- Primary keys: ['id', 'account_id', 'workflow_id']
- Replication strategy: FULL_TABLE



## Authentication

## Quick Start

1. Install

    Clone this repository, and then install using setup.py. We recommend using a virtualenv:

    ```bash
    > virtualenv -p python3 venv
    > source venv/bin/activate
    > python setup.py install
    OR
    > cd .../tap-drip
    > pip install -e .
    ```
2. Dependent libraries. The following dependent libraries were installed.
    ```bash
    > pip install singer-python
    > pip install target-stitch
    > pip install target-json

    ```
    - [singer-tools](https://github.com/singer-io/singer-tools)
    - [target-stitch](https://github.com/singer-io/target-stitch)

3. Create your tap's `config.json` file.  The tap config file for this tap should include these entries:
   - `start_date` - the default value to use if no bookmark exists for an endpoint (rfc3339 date string)
   - `user_agent` (string, optional): Process and email for API logging purposes. Example: `tap-drip <api_user_email@your_company.com>`
   - `request_timeout` (integer, `300`): Max time for which request should wait to get a response. Default request_timeout is 300 seconds.
   - `api_token` (string): Api token which we need to generate from drip account.

    ```json
    {
        "start_date": "2019-01-01T00:00:00Z",
        "user_agent": "tap-drip <api_user_email@your_company.com>",
        "request_timeout": 300,
        "api_token": "dummy api token"
    }

    ```
    Optionally, also create a `state.json` file. `currently_syncing` is an optional attribute used for identifying the last object to be synced in case the job is interrupted mid-stream. The next run would begin where the last job left off.

    ```json
    {
        "currently_syncing": "dummy_stream1",
        "bookmarks": {
            "dummy_stream1": "2019-09-27T22:34:39.000000Z",
            "dummy_stream2": "2019-09-28T15:30:26.000000Z",
            "dummy_stream3": "2019-09-28T18:23:53Z"
        }
    }
    ```

4. Run the Tap in Discovery Mode
    This creates a catalog.json for selecting objects/fields to integrate:
    ```bash
    tap-drip --config config.json --discover > catalog.json
    ```
   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode (with catalog) and [write out to state file](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#running-a-singer-tap-with-a-singer-target)

    For Sync mode:
    ```bash
    > tap-drip --config tap_config.json --catalog catalog.json > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
    To load to json files to verify outputs:
    ```bash
    > tap-drip --config tap_config.json --catalog catalog.json | target-json > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
    To pseudo-load to [Stitch Import API](https://github.com/singer-io/target-stitch) with dry run:
    ```bash
    > tap-drip --config tap_config.json --catalog catalog.json | target-stitch --config target_config.json --dry-run > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```

6. Test the Tap
    While developing the drip tap, the following utilities were run in accordance with Singer.io best practices:
    Pylint to improve [code quality](https://github.com/singer-io/getting-started/blob/master/docs/BEST_PRACTICES.md#code-quality):
    ```bash
    > pylint tap_drip -d missing-docstring -d logging-format-interpolation -d too-many-locals -d too-many-arguments
    ```
    Pylint test resulted in the following score:
    ```bash
    Your code has been rated at 9.67/10
    ```

    To [check the tap](https://github.com/singer-io/singer-tools#singer-check-tap) and verify working:
    ```bash
    > tap_drip --config tap_config.json --catalog catalog.json | singer-check-tap > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```

    #### Unit Tests

    Unit tests may be run with the following.

    ```
    python -m pytest --verbose
    ```

    Note, you may need to install test dependencies.

    ```
    pip install -e .'[dev]'
    ```
---

Copyright &copy; 2019 Stitch
