#!/usr/bin/python3
""" Test module for file_storage module
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test class for FileStorage class
    """
    def test_file_path(self):
        """test file path
        """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)
        self.assertTrue(hasattr(fs, "__file_path"))

    def test_object(self):
        """test object attribute
        """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_new(self):
        """test new method
        """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_all(self):
        """test all method
        """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_save(self):
        """test save method
        """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def reload(self):
        """test reload method
        """
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)
