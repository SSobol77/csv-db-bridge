import unittest
from unittest.mock import patch, MagicMock
import mysql.connector

class TestMySQLImport(unittest.TestCase):

    @patch('mysql.connector.connect')
    def test_mysql_connection_and_insert(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        from import import imp_mysql
        imp_mysql.mysql = mysql  # Patch module inside file

        mock_cursor.execute.assert_not_called()
        mock_cursor.execute("INSERT INTO table (col1, col2) VALUES (%s, %s)", ("val1", "val2"))
        self.assertTrue(mock_connect.called)

if __name__ == '__main__':
    unittest.main()
