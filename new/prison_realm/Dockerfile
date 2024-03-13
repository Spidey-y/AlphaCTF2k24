FROM ubuntu:24.04

RUN apt update && \
    apt install socat strace python3 -y && \
    rm -r /var/lib/apt/lists/*

RUN useradd -mG sudo -s /bin/bash alpha 
WORKDIR /home/alpha
COPY ./challenge/flag.txt ./challenge/prison_setup.sh ./entrypoint.sh ./
RUN mv ./entrypoint.sh / && \
    chmod u+s /usr/sbin/chroot && \
    chown root:root flag.txt && \
    chown root:alpha /entrypoint.sh ./prison_setup.sh && \
    chmod 000 flag.txt && \
    chmod 750 /entrypoint.sh prison_setup.sh && \
    ./prison_setup.sh && rm ./prison_setup.sh

EXPOSE 1000

ENTRYPOINT ["/entrypoint.sh"] 

USER alpha
