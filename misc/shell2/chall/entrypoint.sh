!/bin/bash

EXEC="/home/ctfer/script.sh"
PORT=1337

su - ctfer -s -c "export FLAG=AlphaCTF{N3v3r_f0rget_t0_qu0t3_ur_v4r1abl35} && socat TCP-LISTEN:$PORT,fork SYSTEM:'$EXEC',pty,raw,echo=0,stderr"
