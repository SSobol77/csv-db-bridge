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
