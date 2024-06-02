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
        
        [schedule]
        timezone = "Australia/Sydney"
        notify_time = "09:00"
        """)
        self.temp_file.seek(0)

    def test_load_config(self):
        album_config, schedule_config = load_config(self.temp_file.name)
        self.assertEqual("Test User", album_config.project_name)
        self.assertEqual("you@me.com", album_config.project_email)
        self.assertEqual("Australia/Sydney", schedule_config.timezone)
        self.assertEqual("09:00", schedule_config.time)

    def tearDown(self):
        self.temp_file.close()
