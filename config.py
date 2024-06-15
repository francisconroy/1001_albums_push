import enum
import tomllib
from dataclasses import dataclass
from typing import Tuple


class StreamingServices(enum.StrEnum):
    spotify = "spotify"
    apple_music = "appleMusic"
    # tidal
    # amazonMusic
    # youtubeMusic
    # qobuz
    # deezer


@dataclass
class AlbumsConfig:
    project_name: str
    streaming_service: StreamingServices


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
                project_name=config_data["1001_albums"].get("project_name",
                                                            ""),
                streaming_service=StreamingServices(
                    config_data["1001_albums"].get("streaming_service",))),
            ScheduleConfig(
                time=config_data["schedule"].get("notify_time", ""),
                timezone=config_data["schedule"].get("timezone",
                                                     "")),
            NtfyConfig(topic=config_data["ntfy"].get("topic", ""))
        )
