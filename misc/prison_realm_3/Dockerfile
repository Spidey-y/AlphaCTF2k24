FROM ubuntu:24.04

RUN apt update && \
    apt install socat sudo -y && \
    rm -r /var/lib/apt/lists/*

RUN useradd -mG sudo -s /bin/bash alpha
WORKDIR /home/alpha

COPY ./challenge/flag.txt ./challenge/prison_setup.sh ./
COPY ./entrypoint.sh ./challenge/startup.sh ./challenge/check.sh /
COPY ./challenge/sudoers /etc/sudoers

RUN chown root:root /etc/sudoers flag.txt && chmod ug=r /etc/sudoers &&\
    chown root:alpha /entrypoint.sh /startup.sh /check.sh ./prison_setup.sh &&\
    chmod 000 flag.txt && chmod 760 /entrypoint.sh /startup.sh /check.sh prison_setup.sh &&\
    mkdir /.scripts && chown alpha:alpha /.scripts/ &&\
    mv /entrypoint.sh /.entrypoint.sh && mv /startup.sh /.scripts/.startup.sh && mv /check.sh /.check.sh &&\
    cp -p /.scripts/.startup.sh /.startup_bak.sh && chmod 760 /.startup_bak.sh && ./prison_setup.sh && rm ./prison_setup.sh

EXPOSE 1337

ENTRYPOINT ["/.entrypoint.sh"] 

USER alpha
