FROM ubuntu:24.04 AS chall

RUN apt update && \
    apt install \
    socat \
    cron \
    -y && \
    rm -r /var/lib/apt/lists/*

RUN useradd -md /var/tmp/.tawat/ -s /bin/bash ctf && echo "ctf:ctf" | chpasswd

WORKDIR /var/tmp/.tawat/
COPY ./challenge/ ./

RUN mv flag.txt /root/flag.txt && \
    mv D /root/D_bak && \
    mv check_deleted.sh /var/tmp/check_deleted.sh && \
    mv entrypoint.sh /.entrypoint.sh && \
    mv startup.sh /.startup.sh && \
    chmod 777 /root/D_bak &&\
    chown ctf:ctf /root/D_bak && \ 
    chmod 000 /root/flag.txt && chown root:root /root/flag.txt && \
    chmod a+x /var/tmp/check_deleted.sh && \
    chmod u+x /.entrypoint.sh  /.startup.sh && \
    chmod 333 /tmp && chmod +t /tmp && chmod +s $(which chattr)


WORKDIR /
EXPOSE 1337

ENTRYPOINT ["/.entrypoint.sh"]
