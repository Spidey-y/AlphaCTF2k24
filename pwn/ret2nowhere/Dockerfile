FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN addgroup ctf && adduser --ingroup ctf ctf


WORKDIR /home/ctf

COPY ./challenge .

USER ctf

EXPOSE 1337
CMD ["socat","tcp-l:1337,reuseaddr,fork","EXEC:./ret2nowhere"]
