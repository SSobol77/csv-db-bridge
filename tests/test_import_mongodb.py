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
import pymongo

class TestMongoDBImport(unittest.TestCase):

    @patch('pymongo.MongoClient')
    def test_mongodb_insert(self, mock_client):
        mock_conn = MagicMock()
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_client.return_value = mock_conn
        mock_conn.__getitem__.return_value = mock_db
        mock_db.__getitem__.return_value = mock_collection

        from import import imp_mongodb
        imp_mongodb.pymongo = pymongo

        mock_collection.insert_one({"name": "Alice", "age": 30})
        self.assertTrue(mock_client.called)

if __name__ == '__main__':
    unittest.main()
