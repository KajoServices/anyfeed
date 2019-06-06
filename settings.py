"""Anyfeed settings."""

TLS_HOST = '127.0.0.1'

try:
    from settings_local import *
except ImportError:
    print('\n[WARNING] Cannot find local settings, running on default')
