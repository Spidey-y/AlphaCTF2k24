#!/bin/bash

# Loop through all services in the swarm and shutdown each one
for service in $(docker service ls --format "{{.Name}}"); do
    echo "Shutting down service: $service"
    docker service rm "$service"
done
