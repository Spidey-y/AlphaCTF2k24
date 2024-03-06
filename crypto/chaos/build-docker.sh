#!/bin/sh

docker build -t chaos .

docker run -p 1337:1337 chaos
