"""
project

Handles config and accepts details on what gets edited and how
"""
from dataclasses import dataclass, field

@dataclass
class Camera:
    x: int = 0
    y: int = 0
    width: int = 1080
    height: int = 608
    zoom: float = 1.0


@dataclass
class Keyframe:
    time: float
    camera: Camera


@dataclass
class VideoInfo:
    filename: str = ""
    width: int = 0
    height: int = 0
    fps: float = 0.0
    duration: float = 0.0


@dataclass
class Project:
    video: VideoInfo = field(default_factory=VideoInfo)
    camera: Camera = field(default_factory=Camera)
    keyframes: list[Keyframe] = field(default_factory=list)