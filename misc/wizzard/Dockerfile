FROM python:3.10-alpine

RUN apk update && apk add socat

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x app.py entrypoint.sh && adduser --disabled-password --no-create-home ctf && chown ctf /challenge/*
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]
