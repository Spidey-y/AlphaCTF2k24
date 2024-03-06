#!/bin/sh

docker build -t aes_modes .

docker run -p 1337:1337 aes_modes
