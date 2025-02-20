#!/usr/bin/env python3
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from app import app as application

# Optional: Log that the application has been loaded (useful for debugging)
print("Passenger WSGI: Application is loaded", file=sys.stderr) 