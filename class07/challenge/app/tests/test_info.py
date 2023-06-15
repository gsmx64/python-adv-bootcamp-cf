""" Info Test file for Decorator's Challenge"""
# __doc__ (Info Test file for little app for Decorator´s Challenge)

import unittest

from app.models.info import Info


class TestInfo(unittest.TestCase):
    """
    Class for unittest Info
    """

    def setUp(self):
        """
        Instance the Info()
        """
        self.info = Info()

    def test_credits(self):
        """
        Credits Test
        """
        resolve = self.info.show_credits(False)
        title = 'Decorator´s Challengers'

        self.assertEqual(title, resolve['title'])


if __name__ == '__main__':
    unittest.main()
