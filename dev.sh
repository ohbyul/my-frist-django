#!/bin/bash
docker network create instaclone01
docker run -d -p 9999:5432 -e POSTGRES_DB=service -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=1234 --name instaclone01-db --net instaclone01 postgres
docker build -t instaclone01:test .


# docker 실행
docker run -it -p 9998:8000 -p 9997:3000 -v ${PWD}:/code --rm --name instaclone-01 --net instaclone01 instaclone01:test

# 실행?
python manage.py makemigrations
