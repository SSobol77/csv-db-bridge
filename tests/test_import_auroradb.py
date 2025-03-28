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
import boto3

class TestAuroraDBImport(unittest.TestCase):

    @patch('boto3.client')
    def test_aurora_execution(self, mock_client):
        mock_rds = MagicMock()
        mock_client.return_value = mock_rds
        mock_rds.execute_statement.return_value = {'records': []}

        from import import imp_auroradb
        imp_auroradb.boto3 = boto3

        mock_rds.execute_statement.assert_not_called()
        mock_rds.execute_statement(
            secretArn='...',
            database='...',
            resourceArn='...',
            sql='SELECT * FROM table'
        )

        self.assertTrue(mock_client.called)

if __name__ == '__main__':
    unittest.main()
