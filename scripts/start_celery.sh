#!/usr/bin/env bash

cd src
celery -A djangosetup worker -l debug