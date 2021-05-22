#!/bin/bash
source Conda/bin/activate dj
./tomcat/bin/startup.sh
python Dj/manage.py runserver 0.0.0.0:8000
