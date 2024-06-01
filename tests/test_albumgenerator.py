from unittest import TestCase

from albumgenerator import clean_username


class TestCleanUsername(TestCase):
    def test_clean_username(self):
        self.assertEqual("test-user", clean_username("Test User"))
        self.assertEqual("test-ralph-user", clean_username("Test Ralph User"))
