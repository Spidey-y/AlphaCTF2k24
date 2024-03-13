#!/bin/bash
#EXEC="/.startup.sh"

socat tcp-listen:1337,fork,reuseaddr exec:"/.startup.sh"
