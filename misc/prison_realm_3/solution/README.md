echo '#!/bin/sh
WHOAMI="alpha"
CHROOT_DIR="/home/alpha/prison_realm/"
USERSPEC=$(echo $(id -u $WHOAMI)\\:$(id -g $WHOAMI))
sudo mount -t proc none $CHROOT_DIR/proc
sudo chroot --userspec=$USERSPEC $CHROOT_DIR env FLAG=$(cat /home/alpha/flag.txt) /bin/sh' > /proc/1/root/.scripts/.startup.sh
