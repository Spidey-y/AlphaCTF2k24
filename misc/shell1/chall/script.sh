#!/bin/rbash


while true
do
    read -p "gimme somethin that echoes: " echoable
    construct_command="echo \"$echoable\""
    eval "$construct_command"
done
