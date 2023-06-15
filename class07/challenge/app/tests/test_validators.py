""" Validators Test file for Decorator's Challenge"""
# __doc__ (Validators Test file for little app for Decorator´s Challenge)

import unittest

from app.models.validators import Validators


class TestFilters(unittest.TestCase):
    """
    Class for unittest Validators
    """

    def setUp(self):
        """
        Instance the Validators()
        """
        self.validate = Validators()

    def test_validate_int_true(self):
        """
        Validators Test
        """
        resolve = self.validate.validate_int(7)
        value = 7

        self.assertEqual(value, resolve)

    def test_validate_int_false(self):
        """
        Filters Test
        """
        variable = 'abc'
        resolve = self.validate.validate_int(variable)
        value = f'>>> La variable "{str(variable)}" NO es un entero.'

        self.assertEqual(value, resolve)


if __name__ == '__main__':
    unittest.main()
