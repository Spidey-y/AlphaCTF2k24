#!/bin/sh
EXEC="./chall"
PORT=1234

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive EXEC:"$EXEC",stderr
