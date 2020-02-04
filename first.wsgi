#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/first/")
sys.path.insert(0,"/var/www/first/first/")

import logging
logging.basicConfig(stream=sys.stderr)

from first import app as application
