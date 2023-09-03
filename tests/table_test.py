import shutil
import sys
import os
import unittest

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now you can import your modules
import modules.data_logic as data_logic
import modules.table as table

class TestTableCommands(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a temporary data directory for testing
        cls.test_data_dir = 'data/tests'  # Corrected the path
        os.makedirs(cls.test_data_dir, exist_ok=True)
        data_logic.folder_path = cls.test_data_dir

    @classmethod
    def tearDownClass(cls):
        # Clean up the temporary data directory
        shutil.rmtree(cls.test_data_dir)

    def setUp(self):
        # Create a table for testing
        data_logic.create_table('test_table')

    def tearDown(self):
        # Remove the test table after each test
        data_logic.delete_table('test_table')

    def test_create_table(self):
        result = table.table('create', 'test_table_2')
        self.assertEqual(result, "Successfully created table dataset named test_table_2")

    def test_add_row(self):
        result = table.table('add', 'row', 'test_table', 'row_1')
        self.assertEqual(result, "Successfully added row row_1 to table test_table")

    def test_add_value(self):
        table.table('add', 'row', 'test_table', 'row_1')
        result = table.table('add', 'value', 'test_table', 'row_1', 'value_1')
        self.assertEqual(result, "Successfully added value value_1 to row row_1 inside table named test_table")

    def test_delete_table(self):
        result = table.table('delete', 'test_table')
        self.assertEqual(result, "Successfully deleted table dataset named test_table")

    def test_list_tables(self):
        result = table.table('list', 'table')
        self.assertIn('test_table', result)

    def test_list_rows(self):
        table.table('add', 'row', 'test_table', 'row_1')
        result = table.table('list', 'row', 'test_table')
        self.assertIn('row_1', result)

    def test_list_values(self):
        table.table('add', 'row', 'test_table', 'row_1')
        table.table('add', 'value', 'test_table', 'row_1', 'value_1')
        result = table.table('list', 'values', 'test_table', 'row_1')
        self.assertEqual(result, "Values in row_1 in test_table: value_1")

    def test_remove_row(self):
        table.table('add', 'row', 'test_table', 'row_1')
        result = table.table('remove', 'row', 'test_table', 'row_1')
        self.assertEqual(result, "Successfully removed row row_1 from table test_table")

    def test_rename_row(self):
        table.table('add', 'row', 'test_table', 'row_1')
        result = table.table('rename', 'row', 'test_table', 'row_1', 'new_row_name')
        self.assertEqual(result, "Successfully renamed row row_1 to new_row_name in table test_table")

    def test_rename_table(self):
        result = table.table('rename', 'table', 'test_table', 'new_table_name')
        self.assertEqual(result, "Successfully renamed table test_table to new_table_name")

if __name__ == '__main__':
    unittest.main()
