import os
import json

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    CONFIG_FILE = os.environ.get('APP_CONFIG_FILE', os.path.join(os.path.dirname(__file__), 'config_test.json'))

    # Set submissions directory one level up from the app directory
    SUBMISSIONS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'submissions'))

    @classmethod
    def load_config(cls):
        if os.path.exists(cls.CONFIG_FILE):
            with open(cls.CONFIG_FILE, 'r') as f:
                data = json.load(f)
            cls.SUBMISSIONS_DIR = data.get('SUBMISSIONS_DIR', cls.SUBMISSIONS_DIR)

Config.load_config()
