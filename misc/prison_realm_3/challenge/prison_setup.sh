#!/bin/bash
CHROOT_DIR="prison_realm"
binaries=("dash" "nl" "stat" "env" )
config=()
if [[ -d $CHROOT_DIR ]] ; then
	echo "Chroot directory already exists"
	exit 1
else
	mkdir -p ./$CHROOT_DIR/{home,bin,proc,lib,root,lib64,tmp,etc,var} ./$CHROOT_DIR/usr/{bin,lib,lib64,sbin,var} ./$CHROOT_DIR/usr/lib/x86_64-linux-gnu/ ./$CHROOT_DIR/var/{run,log,lib} 
  chmod 333 ./$CHROOT_DIR/tmp
  chmod +t ./$CHROOT_DIR/tmp
	for binary in ${binaries[@]}
	do
    binary_path=$(which $binary)
		cp $binary_path ./$CHROOT_DIR/usr/bin
		cp $(ldd $binary_path | grep -Po "((?<=> )|/)([^=>])+(?= \()" ) ./$CHROOT_DIR/usr/lib/x86_64-linux-gnu/
		if [[ $binary = "dash" ]]; then
			 cd ./$CHROOT_DIR/usr/bin && ln -s -T dash sh && cd - > /dev/null
		fi
	done
	cp -r $CHROOT_DIR/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 ./$CHROOT_DIR/lib64/
	cp -r $CHROOT_DIR/usr/bin/ ./$CHROOT_DIR/
	cp -r $CHROOT_DIR/usr/lib/ ./$CHROOT_DIR/
  cp -r $CHROOT_DIR/usr/lib64 ./$CHROOT_DIR/
	for file in ${config[@]}
	do
		cp $file ./${CHROOT_DIR}${file}
	done 
fi
