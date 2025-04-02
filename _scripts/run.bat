cd ../backend/
pip install pathlib boto3
py create_env_files.py
cd ..
docker-compose up --build -d