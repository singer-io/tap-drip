import unittest
from unittest.mock import patch, MagicMock
from tap_drip.sync import write_schema, sync, update_currently_syncing

class TestSync(unittest.TestCase):

    def test_write_schema_only_parent_selected(self):
        mock_stream = MagicMock()
        mock_stream.is_selected.return_value = True
        mock_stream.children = ["email_series_subscriber_active", "email_series_subscriber_removed"]
        mock_stream.child_to_sync = []

        client = MagicMock()
        catalog = MagicMock()
        catalog.get_stream.return_value = MagicMock()

        write_schema(mock_stream, client, [], catalog)

        mock_stream.write_schema.assert_called_once()
        self.assertEqual(len(mock_stream.child_to_sync), 0)

    def test_write_schema_parent_child_both_selected(self):
        mock_stream = MagicMock()
        mock_stream.is_selected.return_value = True
        mock_stream.children = ["email_series_subscriber_active", "email_series_subscriber_removed"]
        mock_stream.child_to_sync = []

        client = MagicMock()
        catalog = MagicMock()
        catalog.get_stream.return_value = MagicMock()

        write_schema(mock_stream, client, ["email_series_subscriber_removed"], catalog)

        mock_stream.write_schema.assert_called_once()
        self.assertEqual(len(mock_stream.child_to_sync), 1)

    def test_write_schema_child_selected(self):
        mock_stream = MagicMock()
        mock_stream.is_selected.return_value = False
        mock_stream.children = ["email_series_subscriber_active", "email_series_subscriber_removed"]
        mock_stream.child_to_sync = []

        client = MagicMock()
        catalog = MagicMock()
        catalog.get_stream.return_value = MagicMock()

        write_schema(mock_stream, client, ["email_series_subscriber_removed", "email_series_subscriber_active"], catalog)

        self.assertEqual(mock_stream.write_schema.call_count, 0)
        self.assertEqual(len(mock_stream.child_to_sync), 2)

    @patch("singer.write_schema")
    @patch("singer.get_currently_syncing")
    @patch("singer.Transformer")
    @patch("singer.write_state")
    @patch("tap_drip.streams.abstracts.FullTableStream.sync")
    def test_sync_stream1_called(self, mock_sync, mock_write_state, mock_transformer, mock_get_currently_syncing, mock_write_schema):
        mock_get_currently_syncing.return_value = None
        mock_catalog = MagicMock()
        accounts = MagicMock()
        accounts.stream = "accounts"
        users = MagicMock()
        users.stream = "users"
        mock_catalog.get_selected_streams.return_value = [
            accounts,
            users
        ]
        state = {}

        client = MagicMock()
        client.make_request.return_value = {
            "results": [],
            "meta": {
                "total_pages": 1,
                "page": 1
            }
        }
        config = {}

        sync(client, config, mock_catalog, state)

        self.assertEqual(mock_sync.call_count, 2)

    @patch("singer.write_schema")
    @patch("singer.get_currently_syncing")
    @patch("singer.Transformer")
    @patch("singer.write_state")
    @patch("tap_drip.streams.abstracts.FullTableStream.sync")
    def test_sync_child_selected(self, mock_sync, mock_write_state, mock_transformer, mock_get_currently_syncing, mock_write_schema):
        mock_catalog = MagicMock()
        email_series_subscriber_active_stream = MagicMock()
        email_series_subscriber_active_stream.stream = "email_series_subscriber_active"
        email_series_subscriber_removed_stream = MagicMock()
        email_series_subscriber_removed_stream.stream = "email_series_subscriber_removed"
        mock_catalog.get_selected_streams.return_value = [
            email_series_subscriber_active_stream,
            email_series_subscriber_removed_stream
        ]
        state = {}

        client = MagicMock()
        client.make_request.return_value = {
            "results": [],
            "meta": {
                "total_pages": 1,
                "page": 1
            }
        }
        config = {}

        sync(client, config, mock_catalog, state)

        self.assertEqual(mock_sync.call_count, 1)

    @patch("singer.get_currently_syncing")
    @patch("singer.set_currently_syncing")
    @patch("singer.write_state")
    def test_remove_currently_syncing(self, mock_write_state, mock_set_currently_syncing, mock_get_currently_syncing):
        mock_get_currently_syncing.return_value = "accounts"
        state = {"currently_syncing": "accounts"}

        update_currently_syncing(state, None)

        mock_get_currently_syncing.assert_called_once_with(state)
        mock_set_currently_syncing.assert_not_called()
        mock_write_state.assert_called_once_with(state)
        self.assertNotIn("currently_syncing", state)

    @patch("singer.get_currently_syncing")
    @patch("singer.set_currently_syncing")
    @patch("singer.write_state")
    def test_set_currently_syncing(self, mock_write_state, mock_set_currently_syncing, mock_get_currently_syncing):
        mock_get_currently_syncing.return_value = None
        state = {}

        update_currently_syncing(state, "accounts")

        mock_get_currently_syncing.assert_not_called()
        mock_set_currently_syncing.assert_called_once_with(state, "accounts")
        mock_write_state.assert_called_once_with(state)
        self.assertNotIn("currently_syncing", state)
