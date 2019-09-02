import unittest
import json
import app
from mock import patch

documents = []
directories = {}


def setUpModule():
    with open('../fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('../fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class TestAppDocs(unittest.TestCase):

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)
        self.assertEqual(len(app.get_all_doc_owners_names()), len(documents))

    def test_append_doc_to_shelf(self):
        doc_number = 123
        shelf_number = '3'
        app.append_doc_to_shelf(doc_number=doc_number, shelf_number=shelf_number)
        self.assertIn(doc_number, directories[shelf_number])

    def test_del_doc(self):
        with patch('app.input', return_value="11-2") as _:
            self.assertTrue(app.delete_doc())

    def test_remove_doc_from_shelf(self):
        doc_number = 10006
        shelf_number = '2'
        app.remove_doc_from_shelf(doc_number=doc_number)
        self.assertFalse(doc_number, directories[shelf_number])

    def test_get_doc_owner_name_exist(self):
        with patch('src.app.input', return_value='10006'):
            self.assertEqual(app.get_doc_owner_name(), "Аристарх Павлов")


if __name__ == '__main__':
    unittest.main()
