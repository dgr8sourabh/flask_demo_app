#!/bin/bash

# Set environment variables
export FLASK_APP=run.py
export FLASK_ENV=production

# Run the Gunicorn server with 3 worker processes
exec gunicorn -w 3 -b 0.0.0.0:8000 run:app