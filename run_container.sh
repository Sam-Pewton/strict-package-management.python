#!/usr/bin/bash
docker buildx build -t test_container:latest .
docker run --rm test_container
docker image rm test_container
