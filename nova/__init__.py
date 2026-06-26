from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("nova-lang")
except PackageNotFoundError:
    __version__ = "1.0.2"