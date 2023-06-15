""" Filters Test file for Decorator's Challenge"""
# __doc__ (Filters Test file for little app for Decorator´s Challenge)

import unittest

from app.models.filters import Filters


class TestFilters(unittest.TestCase):
    """
    Class for unittest Filters
    """

    def setUp(self):
        """
        Instance the Filters()
        """
        self.filters = Filters()

    def test_data_type_boolean_true(self):
        """
        Filters Test
        """
        resolve = self.filters.data_type('True')
        value = True

        self.assertEqual(value, resolve)

    def test_data_type_boolean_false(self):
        """
        Filters Test
        """
        resolve = self.filters.data_type('False')
        value = False

        self.assertEqual(value, resolve)

    def test_data_type_integer(self):
        """
        Filters Test
        """
        resolve = self.filters.data_type('15')
        value = 15

        self.assertEqual(value, resolve)

    def test_data_type_float(self):
        """
        Filters Test
        """
        resolve = self.filters.data_type('1.25')
        value = 1.25

        self.assertEqual(value, resolve)

    def test_data_type_string(self):
        """
        Filters Test
        """
        resolve = self.filters.data_type(type('String Text'))
        value = "<class 'str'>"

        self.assertEqual(value, resolve)


if __name__ == '__main__':
    unittest.main()
