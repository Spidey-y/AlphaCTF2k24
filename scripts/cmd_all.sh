#!/bin/sh

ALL_CHALLS_SCRIPT="./all_challs.sh"
DIRNAME="$(
    cd -- "$(dirname "$0")" >/dev/null 2>&1
    pwd -P
)"

for chal in $("${DIRNAME}/${ALL_CHALLS_SCRIPT}"); do
    echo "Challenge: '${chal}'"
    ctf "$@" "${chal}"
done
