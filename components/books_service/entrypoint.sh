#!/usr/bin/env sh

gunicorn run:app --reload -w 1