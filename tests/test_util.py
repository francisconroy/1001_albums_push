from unittest import TestCase
from unittest.mock import patch

from util import PersistentTopic, generate_unique_key


class TestPersistentTopic(TestCase):
    def setUp(self):
        self.topic = PersistentTopic("testuser")

    def test_topic(self):
        self.fail()

    def test_username(self):
        self.fail()


class TestPersistentTopicCreation(TestCase):
    def setUp(self):
        self.user = "Test User"
        persistent_topic = PersistentTopic(self.user)
        self.topic = persistent_topic.topic

    def test_topic_unchanged(self):
        persistent_topic = PersistentTopic(self.user)
        self.assertEqual(self.topic, persistent_topic.topic)

    def test_username_unchanged(self):
        persistent_topic = PersistentTopic(self.user)
        self.assertEqual(self.topic, persistent_topic.topic)

    def test_topic_changes_when_username_does(self):
        persistent_topic = PersistentTopic("Test User Two")
        self.assertNotEqual(self.topic, persistent_topic.topic)


class TestGenerateUniqueKey(TestCase):
    def test_generate_unique_key(self):
        with patch("util.random.choices") as mock_choices:
            mock_choices.return_value = ["one", "two", "three", "four"]
            self.assertEqual("one_two_three_four", generate_unique_key())
