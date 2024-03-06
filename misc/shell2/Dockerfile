
FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' --home /home/ctfer ctfer

WORKDIR /home/ctfer

COPY ./chall .

RUN chown -R ctfer:ctfer /home/ctfer && \
    chmod +x ./script.sh ./entrypoint.sh 

ENTRYPOINT ["./entrypoint.sh"]
