#!/bin/bash

# Set environment variables
export PYTHONPATH=$PYTHONPATH:"/home/site/wwwroot/venv/lib/python3.9/site-packages"
GUNICORN_CMD_ARGS="--timeout 600 --access-logfile '-' --error-logfile '-' --chdir=/home/site/wwwroot"


# Run the Gunicorn server with 3 worker processes
gunicorn --bind=0.0.0.0 --timeout 600 --chdir==/home/site/wwwroot run:app