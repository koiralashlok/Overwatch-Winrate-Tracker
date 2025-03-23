#!/bin/bash

cd ../backend/
sudo pip install pathlib
sudo python3 create_env_files.py
cd ..
sudo docker-compose up --build -d