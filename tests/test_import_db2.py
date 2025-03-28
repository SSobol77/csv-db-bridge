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
import ibm_db

class TestDB2Import(unittest.TestCase):

    @patch('ibm_db.connect')
    def test_db2_connection(self, mock_connect):
        mock_conn = MagicMock()
        mock_stmt = MagicMock()
        mock_connect.return_value = mock_conn
        with patch('ibm_db.exec_immediate', return_value=mock_stmt):
            with patch('ibm_db.fetch_assoc', return_value={"col1": "val"}):
                from import import imp_db2
                imp_db2.ibm_db = ibm_db
                self.assertTrue(mock_connect.called)

if __name__ == '__main__':
    unittest.main()
