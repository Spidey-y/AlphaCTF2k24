FROM python:3-alpine

RUN apk update && \
    apk add socat

RUN useradd ctf 

WORKDIR /challenge

COPY challenge /challenge/

RUN chown -R root:root . && \
    chmod +x challenge.py entrypoint.sh

EXPOSE 1114

USER ctf

ENTRYPOINT ["./entrypoint.sh"]