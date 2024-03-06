#!/bin/sh

docker build -t ez_aes .

docker run -p 1337:1337 ez_aes
