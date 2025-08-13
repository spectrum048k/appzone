import os
import json

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    CONFIG_FILE = os.environ.get('APP_CONFIG_FILE', os.path.join(os.path.dirname(__file__), 'config_test.json'))

    @classmethod
    def load_config(cls):
        if os.path.exists(cls.CONFIG_FILE):
            with open(cls.CONFIG_FILE, 'r') as f:
                data = json.load(f)
            cls.SUBMISSIONS_DIR = data.get('SUBMISSIONS_DIR', os.path.join(os.path.dirname(__file__), 'submissions'))
        else:
            cls.SUBMISSIONS_DIR = os.path.join(os.path.dirname(__file__), 'submissions')

Config.load_config()
