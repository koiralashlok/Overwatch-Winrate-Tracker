import json
import os
from pathlib import Path
from aws_utils import AWSUtils

# If secrets exist, don't go to AWS param store
BASE_DIR = Path(__file__).resolve().parent
secrets_file = BASE_DIR / 'backend-secrets.json'
if not os.path.isfile(secrets_file):
    utils = AWSUtils()
    ec2_ip = utils.get_ssm_parameter('/ow_winrate_tracker/backend_url')
    db_key = utils.get_ssm_parameter('/db/secret-key')
    debug_mode = utils.get_ssm_parameter('ow_winrate_tracker/debug_mode')
else:
    with open(secrets_file, 'r') as file:
        data = json.load(file)
        ec2_ip = data['EC2_IP']
        db_key = data['DB_SECRET_KEY']
        debug_mode = data['DEBUG_MODE']

# Write to env file and load it
with open(BASE_DIR / '.env', 'w') as be_env:
    be_env.writelines(f'EC2_IP={ec2_ip}')
    be_env.writelines(f'DB_SECRET_KEY={db_key}')
    be_env.writelines(f'DEBUG_MODE={debug_mode}')

# Create env file for FE
with open(BASE_DIR.parent / 'frontend' / '.env', 'w') as fe_env:
    fe_env.writelines(f'REACT_APP_BACKEND_URL=http://{ec2_ip}:8000/tracker')