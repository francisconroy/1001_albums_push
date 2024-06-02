import os
import random
import shelve

from albumgenerator import clean_username


def generate_unique_key():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'word_list.txt')
    with open(filename) as wordsfile:
        words = [word.strip() for word in wordsfile.readlines()]
    randwords = random.choices(words, k=4)
    return "_".join(randwords)


def generate_unique_topic(username):
    return f"1001_albums_{clean_username(username)}_" + generate_unique_key()


class PersistentTopic:
    topic_file = "topic"

    def __init__(self, username):
        # check for existing topic
        self.topic_db = shelve.open(self.topic_file)
        existing_username = self.topic_db.setdefault("username", username)
        if existing_username != username:
            self.topic_db["username"] = username
            self.topic_db["topic"] = generate_unique_topic(username)
        if self.topic_db.setdefault("topic", None) is None:
            self.topic_db["topic"] = generate_unique_topic(username)
        self.topic_db.sync()

    @property
    def topic(self):
        return self.topic_db["topic"]

    @property
    def username(self):
        return self.topic_db["username"]
