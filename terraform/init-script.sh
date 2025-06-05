#!/bin/bash
sudo apt update -y
sudo apt install -y docker.io
docker run -d -p 8000:8000 your-dockerhub-user/itsm-ml-app:latest
