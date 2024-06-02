import tempfile
import unittest

from config import load_config


class TestLoadConfig(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w+')
        self.temp_file.write("""
        title = "1001_albums_push_config"

        [1001_albums]
        project_name = "Test User"
        project_email = "you@me.com"
        """)
        self.temp_file.seek(0)

    def test_load_config(self):
        config = load_config(self.temp_file.name)
        self.assertEqual(config.project_name, "Test User")
        self.assertEqual(config.project_email, "you@me.com")

    def tearDown(self):
        self.temp_file.close()
