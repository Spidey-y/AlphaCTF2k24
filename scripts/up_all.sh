#!/bin/bash

folders=(web misc pwn)

for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo "Entering folder: $folder"
        cd "$folder"

        for subfolder in */; do
            if [ -f "$subfolder/docker-compose.yml" ]; then
                echo "Found docker-compose.yml in $subfolder"
                cd "$subfolder"
                docker-compose up --build -d
                cd ..
            fi
        done
        cd ..
    else
        echo "Folder does not exist: $folder"
    fi
done