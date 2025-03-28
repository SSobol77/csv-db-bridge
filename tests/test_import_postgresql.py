import unittest
from unittest.mock import patch, MagicMock
import psycopg2

class TestPostgresImport(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_import_inserts_data(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Simulate execution of insert statement
        from import import imp_postgresql
        imp_postgresql.psycopg2 = psycopg2  # Needed for patching inside imported file

        mock_cursor.execute.assert_not_called()
        mock_cursor.execute("INSERT INTO mytable VALUES (%s, %s)", ("val1", "val2"))
        mock_conn.commit.assert_not_called()  # as we don't commit in test

        self.assertTrue(mock_connect.called)

if __name__ == '__main__':
    unittest.main()
