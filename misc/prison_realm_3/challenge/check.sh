#!/bin/sh
REGEX='#!\/bin\/sh\nWHOAMI="alpha"\nCHROOT_DIR="\/home\/alpha\/prison_realm\/"\nUSERSPEC=\$\(echo \$\(id -u \$WHOAMI\)\\:\$\(id -g \$WHOAMI\)\)\nsudo mount -t proc none \$CHROOT_DIR\/proc\nsudo chroot --userspec=\$USERSPEC \$CHROOT_DIR( | [^;]+ )\/bin\/sh'

if grep -q -Pz "$REGEX" /.scripts/.startup.sh ; then
  /.scripts/.startup.sh
  cp -p /.startup_bak.sh /.scripts/.startup.sh 
else
  echo "Wrong File Format"
  cp -p /.startup_bak.sh /.scripts/.startup.sh
  /.scripts/.startup.sh
fi
