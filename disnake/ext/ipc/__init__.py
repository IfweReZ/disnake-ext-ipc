import collections

from disnake.ext.ipc.client import Client
from disnake.ext.ipc.server import Server
from disnake.ext.ipc.errors import *


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "2.1.1"
version_info = _VersionInfo(2, 1, 1, "final", 0)
