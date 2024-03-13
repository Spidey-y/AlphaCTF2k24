FROM ubuntu:18.04

RUN apt-get update && apt-get install -y gcc socat

RUN addgroup ctf && adduser --ingroup ctf ctf


WORKDIR /home/ctf
COPY ./challenge .
RUN chown ctf:ctf /home/ctf/ph03n1x && chmod +x ./ph03n1x
USER ctf


EXPOSE 1337
    CMD ["socat","tcp-l:1337,reuseaddr,fork","EXEC:./ph03n1x"]