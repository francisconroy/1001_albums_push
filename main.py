import logging
import time
from typing import Dict

import requests
import schedule

import albumgenerator
from albumgenerator import AlbumData
from config import load_config
from util import PersistentTopic


def prepare_message(album_data: AlbumData) -> (str, Dict):
    message = f"""New album for today!
Album: {album_data.album_name}
Artist: {album_data.album_artist}
Released: {album_data.album_release}
"""
    headers = {
        "Click": album_data.spotify_url,
        "Tags": "loudspeaker,cd",
        "Attach": album_data.cover_url,
    }
    return message, headers


def post_to_topic(topic, message, headers):
    requests.post(f"https://ntfy.sh/{topic}",
                  data=message,
                  headers=headers)


def main():
    # Set up topic
    config = load_config("config.toml")
    topic_data = PersistentTopic(config.project_name)
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Using topic {topic_data.topic}")

    url = albumgenerator.get_project_url(config.project_name)
    api_data = albumgenerator.get_api_json(url)
    album_data = albumgenerator.extract_album_data(api_data)
    message, headers = prepare_message(album_data)
    post_to_topic(topic_data.topic, message, headers)
    #
    # def job():
    #     # connect to 1001 albums generator
    #     print(config.project_name)
    #     # get today's album
    #     # push the link to your phone
    #     pass
    #
    # schedule.every().day.at("10:30").do(job)
    # schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
    #
    # def job_with_argument(name):
    #     print(f"I am {name}")
    #
    # schedule.every(10).seconds.do(job_with_argument, name="Peter")
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == "__main__":
    main()