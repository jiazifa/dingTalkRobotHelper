#!/bin/sh
set -e
PORT=${PORT:-5000}
gunicorn -b :${PORT} -w 4 app:app
