#!/bin/sh

EXEC="./challenge.py"
PORT=2323

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr