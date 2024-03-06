#!/bin/sh 
EXEC="/.check.sh"
PORT=1337
sudo socat -v -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive,ignoreeof exec:"$EXEC",stderr
