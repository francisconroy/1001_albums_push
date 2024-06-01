from dataclasses import dataclass
from typing import Dict

import requests


def get_project_url(username):
    return f"https://1001albumsgenerator.com/api/v1/projects/{clean_username(username)}"


def clean_username(username):
    return username.lower().strip().replace(" ", "-")


def get_api_json(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("API request failed")


@dataclass
class AlbumData:
    spotify_id: str
    album_name: str
    album_artist: str
    album_release: str


def extract_album_data(dictdata: Dict) -> AlbumData:
    current_album_data = dictdata['currentAlbum']
    return AlbumData(spotify_id=current_album_data['spotifyId'],
                     album_name=current_album_data['name'],
                     album_artist=current_album_data['artist'],
                     album_release=current_album_data['releaseDate'])


if __name__ == "__main__":
    data = get_api_json(get_project_url("Francis Conroy"))
    pass
