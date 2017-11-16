#!/bin/bash

settings=${1:-"dbsupport.settings"}
ip=${2:-"10.31.145.247"}
port=${3:-8888}

/app/python36/bin/gunicorn -w 2 --env DJANGO_SETTINGS_MODULE=${settings} --error-logfile=/data/dbsupport/log/dbsupport.err -b ${ip}:${port} --daemon dbsupport.wsgi:application --timeout 1200
