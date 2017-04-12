#!/bin/bash
docker exec -it $1 install.sh
docker exec -it $1 python /tibero/scripts/createdb.py
