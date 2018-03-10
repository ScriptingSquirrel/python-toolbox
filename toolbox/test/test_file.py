import tempfile
import unittest
from pathlib import Path

from toolbox import file


class Test_touch(unittest.TestCase):

    def setUp(self):
        self._temporary_directory_object = tempfile.TemporaryDirectory()
        self.empty_directory_path = Path(self._temporary_directory_object.name)

    def tearDown(self):
        self._temporary_directory_object.cleanup()

    def test___touch_non_existing_file___expect_file_exists_afterwards(self):
        file_path = self.empty_directory_path.joinpath('a_new_file')

        file_exists_before = file_path.exists()
        self.assertFalse(file_exists_before)

        file.touch(file_path)

        file_exists_after = file_path.exists()
        self.assertTrue(file_exists_after)

    def test___touch_non_existing_file_with_path_as_str___expect_file_exists_afterwards(self):
        file_path = self.empty_directory_path.joinpath('a_new_file')
        file_path_as_str = str(file_path)

        file_exists_before = file_path.exists()
        self.assertFalse(file_exists_before)

        file.touch(file_path_as_str)

        file_exists_after = file_path.exists()
        self.assertTrue(file_exists_after)

    def test___touch_existing_file___expect_file_contents_not_changed(self):
        file_path = self.empty_directory_path.joinpath('a_new_file')

        file_contents_before = 'test\nsomething'
        with open(file_path, 'w') as file_stream:
            file_stream.write(file_contents_before)

        file.touch(file_path)

        with open(file_path, 'r') as file_stream:
            file_contents_afterwards = file_stream.read()

        self.assertEqual(file_contents_before, file_contents_afterwards)
