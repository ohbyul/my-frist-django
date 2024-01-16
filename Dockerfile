FROM node:17.9-alpine3.14

# RUN apk add --no-cache python g++ make
RUN apk add --no-cache python3 py3-pip
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev

RUN ln -sf python3 /usr/bin/python

ENV CHOKIDAR_USEPOLLING=true 

WORKDIR /code
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

ENTRYPOINT ["ash"]