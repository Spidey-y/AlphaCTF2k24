#!/bin/sh

docker build -t lost_admin .

docker run -p 1337:1337 lost_admin
