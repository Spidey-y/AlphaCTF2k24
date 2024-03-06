FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat 

RUN useradd ctf 

WORKDIR /challenge

COPY challenge .

RUN chown -R root:root .
RUN chmod +x chall entrypoint.sh

EXPOSE 1337

USER ctf

ENTRYPOINT [ "./entrypoint.sh" ]