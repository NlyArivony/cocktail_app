#!/bin/bash

# Build the Docker image
docker build -t cocktail_app .

# Run the Docker container and map the container port to localhost
docker run -p 5000:5000 cocktail_app