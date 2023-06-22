""" Filters test file for Multi_Maths Package """
# __doc__ (Filters test file for testing modules and packages)

import configparser
from pathlib import Path
import unittest

from multi_maths.filters import Filters


class TestFilters(unittest.TestCase):
    """
    Class for unittest Filters
    """

    def setUp(self):
        """
        Instance the filters()
        """
        lang_file = Path('../multi_maths/languages/en.ini')
        self.lang = configparser.ConfigParser()
        self.lang.sections()
        self.lang.read(lang_file, 'UTF-8')

        self.filters = Filters(self.lang)

    def test_filters_value(self):
        """
        Credits Test
        """
        test = self.filters.value('15.0')
        resolve = 15.0

        self.assertEqual(test, resolve)

    def test_filters_is_float(self):
        """
        Credits Test
        """
        test = self.filters.value('15.0')
        resolve = 15.0

        self.assertAlmostEqual(test, resolve)


if __name__ == '__main__':
    unittest.main()
