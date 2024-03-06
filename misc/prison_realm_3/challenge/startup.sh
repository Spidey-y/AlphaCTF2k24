#!/bin/sh
WHOAMI="alpha"
CHROOT_DIR="/home/alpha/prison_realm/"
USERSPEC=$(echo $(id -u $WHOAMI)\:$(id -g $WHOAMI))
sudo mount -t proc none $CHROOT_DIR/proc
sudo chroot --userspec=$USERSPEC $CHROOT_DIR /bin/sh
