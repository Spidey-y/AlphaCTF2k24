#!/bin/sh

docker build -t www .

docker run -p 1337:1337 www
