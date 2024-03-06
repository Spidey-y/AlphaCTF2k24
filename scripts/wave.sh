#!/bin/bash

# List of paths to Docker Compose files for list 1
compose_paths_2=(
  "./web/SQLi_1/docker-compose.yml"
  "./web/SQLi_2/docker-compose.yml"
  "./web/SQLi_3/docker-compose.yml"
  "./web/SQLi_4/docker-compose.yml"
  "./web/login/docker-compose.yml"
  "./misc/Secret/docker-compose.yml"
  "./misc/yaml/docker-compose.yml"
  "./pwn/echo/docker-compose.yml"

)

compose_paths_1=(
  "./web/bigHEAD/docker-compose.yml"
  "./web/fREe/docker-compose.yml"
  "./web/weird/docker-compose.yml"
  "./web/Inspector/docker-compose.yml"
  "./web/PingPong1/docker-compose.yml"
  "./web/PingPong2/docker-compose.yml"
  "./misc/matrix/docker-compose.yml"
  "./misc/Path/docker-compose.yml"
  "./misc/Autobash/docker-compose.yml"
  "./pwn/Crash/docker-compose.yml"
  "./pwn/DeadBeef/docker-compose.yml"
  "./pwn/ret2win/docker-compose.yml"
)

compose_paths_3=(
  "./web/blogger/docker-compose.yml"
  "./misc/py1/docker-compose.yml"
  "./misc/py2/docker-compose.yml"
  "./misc/Guess/docker-compose.yml"
  "./crypto/flagger/docker-compose.yml"
)
# Check if an integer argument was passed
if [[ ! $1 =~ ^[0-9]+$ ]]; then
  echo "Please provide an integer argument."
  exit 1
fi

# Choose the list of paths based on the input integer
if (( $1 == 1 )); then
  compose_paths=("${compose_paths_1[@]}")
elif (( $1 == 2 )); then
  compose_paths=("${compose_paths_2[@]}")
elif (( $1 == 3 )); then
  compose_paths=("${compose_paths_3[@]}")
else
  echo "Invalid integer argument. Please choose 1 or 2."
  exit 1
fi

# Iterate through the list of Docker Compose paths and run docker-compose up
for path in "${compose_paths[@]}"; do
  echo "Running Docker Compose for $path"
  docker-compose -f "$path" up --build -d
done