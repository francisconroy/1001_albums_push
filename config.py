import tomllib
from dataclasses import dataclass


@dataclass
class AlbumsConfig:
    project_name: str
    project_email: str


def load_config(path) -> AlbumsConfig:
    with open(path, 'rb') as tomlfp:
        config_data = tomllib.load(tomlfp)
        return AlbumsConfig(
            project_name=config_data["1001_albums"].get("project_name", ""),
            project_email=config_data["1001_albums"].get("project_email", ""))
