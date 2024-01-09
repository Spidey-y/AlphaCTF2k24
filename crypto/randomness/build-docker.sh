#!/bin/sh

docker build -t randomness .

docker run -p 1337:1337 randomness
