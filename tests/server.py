#!/usr/bin/env python
import os
from swampdragon.swampdragon_server import run_server

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ci.settings")

run_server()