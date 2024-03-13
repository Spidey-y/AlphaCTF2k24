#!/bin/sh

docker build -t card_trick .

docker run -p 1337:1337 card_trick
