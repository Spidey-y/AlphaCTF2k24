FROM python:2-alpine

RUN apk update && \
    apk add socat

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x challenge.py entrypoint.sh
EXPOSE 1114
ENTRYPOINT ["./entrypoint.sh"]