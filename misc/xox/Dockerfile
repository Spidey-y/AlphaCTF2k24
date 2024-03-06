FROM python:3-alpine

RUN apk update && \
    apk add socat

COPY challenge /challenge/

WORKDIR /challenge

RUN chmod +x challenge.py entrypoint.sh

EXPOSE 2323

ENTRYPOINT ["./entrypoint.sh"]
