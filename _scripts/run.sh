#!/bin/bash

cd ../backend/
pip install pathlib
python create_env_files.py
cd ..
docker-compose up --build -d