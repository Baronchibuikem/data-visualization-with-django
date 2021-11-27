#!/usr/bin/env bash

cd src
celery -A djangosetup beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler