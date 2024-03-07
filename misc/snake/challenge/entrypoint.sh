#!/bin/sh

EXEC="./challenge.py"
PORT=1114

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr