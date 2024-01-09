#!/bin/sh

docker build -t chunks .

docker run -p 1234:1234 chunks
