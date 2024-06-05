import tomllib
from dataclasses import dataclass
from typing import Tuple


@dataclass
class AlbumsConfig:
    project_name: str
    project_email: str


@dataclass
class ScheduleConfig:
    time: str
    timezone: str

@dataclass
class NtfyConfig:
    topic: str


def load_config(path) -> Tuple[AlbumsConfig, ScheduleConfig, NtfyConfig]:
    with open(path, 'rb') as tomlfp:
        config_data = tomllib.load(tomlfp)
        return (
            AlbumsConfig(
                project_name=config_data["1001_albums"].get("project_name", ""),
                project_email=config_data["1001_albums"].get("project_email",
                                                             "")),
            ScheduleConfig(time=config_data["schedule"].get("notify_time", ""),
                           timezone=config_data["schedule"].get("timezone",
                                                                "")),
            NtfyConfig(topic=config_data["ntfy"].get("topic", ""))
        )
