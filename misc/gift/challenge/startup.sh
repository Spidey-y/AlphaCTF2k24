#!/bin/bash
TEMP_DIR=$(mktemp -d)
CRON_JOB=$(echo $TEMP_DIR | cut -d / -f 3 )
chown ctf:ctf $TEMP_DIR
cp -p /root/D_bak $TEMP_DIR/D
chattr +i $TEMP_DIR/D
echo "* * * * * /var/tmp/check_deleted.sh $TEMP_DIR" >> /etc/cron.d/$CRON_JOB
crontab /etc/cron.d/$CRON_JOB
cron
su - ctf --command "cd $TEMP_DIR && /bin/rbash"
rm /etc/cron.d/$CRON_JOB
chattr -i $TEMP_DIR/D
rm -rf $TEMP_DIR
