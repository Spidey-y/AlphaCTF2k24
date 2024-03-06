#!/bin/sh

docker build -t enigma .

docker run -p 1337:1337 enigma
