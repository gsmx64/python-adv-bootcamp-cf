""" Decorator Test file for Decorator's Challenge"""
# __doc__ (Decorator Test file for little app for Decorator´s Challenge)

import unittest

from app.models.filters import Filters
from app.decorators.decorator import decorator_validate_int


class TestDecorator(unittest.TestCase):
    """
    Class for unittest Decorator
    """

    def setUp(self):
        """
        Instance the Decorator()
        """
        self.filters = Filters()

    @decorator_validate_int
    def add(self, var_a, var_b):
        """
        Decorator
        """
        return var_a + var_b

    def test_decorator_ok(self):
        """
        Decorator Test
        """
        value1 = self.filters.data_type(2)
        value2 = self.filters.data_type('3')

        resolve = self.add(value1, value2)
        value = 5

        self.assertEqual(value, resolve)

    def test_decorator_error(self):
        """
        Decorator Test
        """
        value1 = self.filters.data_type('1.1')
        value2 = self.filters.data_type('1')

        resolve = self.add(value1, value2)
        value = """Error de Tipo: Operación de Tipo no soportada al """
        value += """sumar 2 variables de distinto tipo."""
        value += f"""Type Error: >>> La variable "{value2}" NO es un entero."""

        self.assertEqual(value, resolve)


if __name__ == '__main__':
    unittest.main()
