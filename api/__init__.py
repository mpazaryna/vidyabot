from importlib.metadata import version

try:
    __version__ = version("vidyabot")
except ImportError:
    __version__ = "unknown"
