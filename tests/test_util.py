from unittest import TestCase

from util import PersistentTopic


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
