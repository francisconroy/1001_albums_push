import argparse
import logging
import time
from typing import Dict

import requests
import schedule

import albumgenerator
from albumgenerator import AlbumData
from config import load_config, AlbumsConfig, ScheduleConfig, NtfyConfig


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


def log_configuration(album_config: AlbumsConfig,
                      schedule_config: ScheduleConfig,
                      ntfy_config: NtfyConfig):
    logging.info(f"Configuration:")
    logging.info(f"Albumgenerator config:\n{album_config}")
    logging.info(f"Schedule config:\n{schedule_config}")
    logging.info(f"NTFY.sh config:\n{ntfy_config}")


def notifcation_job(config_path: str) -> None:
    logging.info("Running the scheduled daily job")
    logging.info("Loading configuration")
    album_config, schedule_config, ntfy_config = load_config(config_path)
    log_configuration(album_config, schedule_config, ntfy_config)

    url = albumgenerator.get_project_url(album_config.project_name)
    api_data = albumgenerator.get_api_json(url)
    album_data = albumgenerator.extract_album_data(api_data)
    message, headers = prepare_message(album_data)
    logging.info(f"Sending today's notification: {message}")
    post_to_topic(ntfy_config.topic, message, headers)


def main():
    parser = argparse.ArgumentParser(
        prog='1001 albums push notifications',
        description='Pushes a daily notification for your 1001 albums project')
    parser.add_argument('-c', '--config', type=str, default='conf/config.toml',
                        help='The path to the config file')
    args = parser.parse_args()

    album_config, schedule_config, ntfy_config = load_config(args.config)
    logging.basicConfig(level=logging.INFO)
    log_configuration(album_config, schedule_config, ntfy_config)

    # Grab the album generator API content to confirm it's a valid project
    url = albumgenerator.get_project_url(album_config.project_name)
    api_data = albumgenerator.get_api_json(url)
    album_data = albumgenerator.extract_album_data(api_data)
    message, headers = prepare_message(album_data)
    logging.info(f"The last album was:\n{message}")


    schedule.every().day.at(schedule_config.time, schedule_config.timezone).do(
        notifcation_job,
        config_path=args.config)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
