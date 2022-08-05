#!usr/bin/python3
"""Test file for class user"""


import unittest
from models.user import User
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test Caeses"""


    def test_create_instance(self):
        """create new instance"""
        new_user = User()
        self.assertIsInstance(new_user, User)


    def test_create_instance2(self):
        """create new instance"""
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)


if __name__ == '__main__':
    unittest.main()
