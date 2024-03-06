#!/bin/bash

PASSWORD=$FLAG

read -s -p "Enter password: " USER_INPUT

if [[ $PASSWORD == $USER_INPUT ]];then
    echo "Nice job, but did you get the flag?"
else
    echo "So far away."
fi
