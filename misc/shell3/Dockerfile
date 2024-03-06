FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' --shell /bin/rbash --home /home/ctfer ctfer && \
    mkdir -p /home/ctfer/bin

WORKDIR /home/ctfer

COPY ./chall .

RUN chown -R ctfer:ctfer /home/ctfer && \
    chmod +x ./script.sh ./entrypoint.sh && \
    rm /usr/bin/env /usr/bin/printenv && \
    ln -s /usr/bin/socat /home/ctfer/bin && \
    ln -s /usr/bin/tr /home/ctfer/bin && \
    ln -s /bin/sed /home/ctfer/bin && \
    ln -s /bin/grep /home/ctfer/bin && \
    echo 'export PATH=$HOME/bin' > /home/ctfer/.bashrc

ENTRYPOINT ["./entrypoint.sh"]
