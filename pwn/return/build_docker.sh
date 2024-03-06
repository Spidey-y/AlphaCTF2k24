#!/bin/sh

docker build -t return .

docker run -p 1234:1234 return
