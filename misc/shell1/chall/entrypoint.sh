#!/bin/bash

EXEC="/home/ctfer/script.sh"
PORT=1337

su - ctfer -s /bin/rbash -c "export FLAG='AlphaCTF{that_was_ez_ghir_azha_brk}' && export PATH=/home/ctfer/bin && socat TCP-LISTEN:$PORT,fork SYSTEM:'$EXEC',pty,raw,echo=0,stderr"
