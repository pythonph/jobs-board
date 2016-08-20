#!/bin/bash
cd /srv/app
pip3 install -r requirements.txt
npm install
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
