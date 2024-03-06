#!/bin/bash

folders=(web misc pwn crypto)

for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo "Entering folder: $folder"
        cd "$folder"

        for subfolder in */; do
            if [ -f "$subfolder/docker-compose.yml" ]; then
                echo "Found docker-compose.yml in $subfolder"
                cd "$subfolder"
                docker stack deploy -c docker-compose.yml "$folder-$subfolder"
                cd ..
            fi
        done
        cd ..
    else
        echo "Folder does not exist: $folder"
    fi
done
