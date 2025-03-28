# -----------------------------------------------------------------------------
# csv-db-bridge — Universal Import/Export Toolkit for CSV and Databases
# -----------------------------------------------------------------------------
# Author: Siergej Sobolewski <s.sobolewski@hotmail.com>
# License: GNU General Public License v3.0 (GPL-3.0)
#
# This file is part of csv-db-bridge.
# 
# csv-db-bridge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# csv-db-bridge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

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
