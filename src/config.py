import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()

def get_key(key_name):
    return os.getenv(key_name)

def get_data_dir():
    return get_key('DATA_DIR') or './data'
