import unittest
from importlib import import_module
component = import_module('services.sources')


class SourcesTest(unittest.TestCase):

    # Actions

    def setUp(self):
        pass

    # Tests

    def test_make_start_urls(self):
        self.assertEqual(
            component.make_start_urls('base'),
            [r'base?lup_s=01%2F01%2F2005&lup_e=01%2F01%2F2006'])

    def test_make_pattern(self):
        self.assertTrue(component.make_pattern('base'))
