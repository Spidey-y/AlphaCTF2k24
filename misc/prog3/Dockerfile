FROM python:3-alpine

RUN apk update && apk add socat && pip install inputimeout && pip install numpy

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x chall.py entrypoint.sh && adduser --disabled-password --no-create-home ctf && chown ctf chall.py
EXPOSE 1337
ENTRYPOINT ["./entrypoint.sh"]
