import os.path
import unittest

from config import load_config


class TestLoadConfig(unittest.TestCase):
    def setUp(self):
        config_file_path = "../conf/config.toml"
        current_file_path = os.path.dirname(__file__)
        rel_config_file_path = os.path.normpath(
            os.path.join(current_file_path, config_file_path))

        self.config_file = open(rel_config_file_path, mode='r')

    def test_load_config(self):
        album_config, schedule_config, ntfy_config = load_config(
            self.config_file.name)
        self.assertEqual("Francis Conroy", album_config.project_name)
        self.assertEqual("Australia/Sydney", schedule_config.timezone)
        self.assertEqual("09:00", schedule_config.time)
        self.assertEqual(
            "1001_albums_francis-conroy_effect_until_behavior_want",
            ntfy_config.topic)

    def tearDown(self):
        self.config_file.close()
