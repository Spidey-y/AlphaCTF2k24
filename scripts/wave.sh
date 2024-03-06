#!/bin/bash

# List of paths to Docker Compose files for list 1
stack_paths_2=(
    "./web/SQLi_1/docker-compose.yml"
    "./web/SQLi_2/docker-compose.yml"
)

stack_paths_1=(
    "./web/bigHEAD/docker-compose.yml"
    "./web/fREe/docker-compose.yml"

)

stack_paths_3=(
    "./web/blogger/docker-compose.yml"
)

# Check if an integer argument was passed
if [[ ! $1 =~ ^[0-9]+$ ]]; then
    echo "Please provide an integer argument."
    exit 1
fi

# Choose the list of paths based on the input integer
if (($1 == 1)); then
    stack_paths=("${stack_paths_1[@]}")
elif (($1 == 2)); then
    stack_paths=("${stack_paths_2[@]}")
elif (($1 == 3)); then
    stack_paths=("${stack_paths_3[@]}")
else
    echo "Invalid integer argument. Please choose 1, 2, or 3."
    exit 1
fi

# Iterate through the list of Docker Stack paths and deploy the stack
for path in "${stack_paths[@]}"; do
    echo "Deploying Docker Stack for $path"
    stack_name=$(basename "$(dirname "$path")")
    docker stack deploy -c "$path" "$stack_name"
done
