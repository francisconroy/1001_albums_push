from dataclasses import dataclass
from typing import Dict

import requests


def get_project_api_url(username):
    return f"https://1001albumsgenerator.com/api/v1/projects/{clean_username(username)}"


def get_project_main_url(username):
    return f"https://1001albumsgenerator.com/{clean_username(username)}"


def get_project_unpause_url(username):
    return f"https://1001albumsgenerator.com/api/project/{clean_username(username)}/paused"


def clean_username(username):
    return username.lower().strip().replace(" ", "-")


def get_api_json(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("API request failed")


def get_project_page(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception("HTTP request failed")


def unpause_project(username):
    url = get_project_unpause_url(username)
    r = requests.post(url, json={"paused": False})
    if r.status_code != 200:
        raise Exception("HTTP request failed")


def generate_spotify_app_url(spotify_id: str) -> str:
    return f"spotify:album:{spotify_id}"


@dataclass
class AlbumData:
    spotify_id: str
    album_name: str
    album_artist: str
    album_release: str
    cover_url: str

    @property
    def spotify_url(self) -> str:
        return generate_spotify_app_url(self.spotify_id)


def extract_album_data(dictdata: Dict) -> AlbumData:
    current_album_data = dictdata['currentAlbum']
    return AlbumData(spotify_id=current_album_data['spotifyId'],
                     album_name=current_album_data['name'],
                     album_artist=current_album_data['artist'],
                     album_release=current_album_data['releaseDate'],
                     cover_url=current_album_data['images'][-1]['url'])
