import os
import json

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    CONFIG_FILE = os.environ.get('APP_CONFIG_FILE', os.path.join(os.path.dirname(__file__), 'config_test.json'))

    # Set config directory one level up from the app directory
    CONFIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))

    @classmethod
    def load_config(cls):
        if os.path.exists(cls.CONFIG_FILE):
            with open(cls.CONFIG_FILE, 'r') as f:
                data = json.load(f)
            cls.CONFIG_DIR = data.get('CONFIG_DIR', cls.CONFIG_DIR)

Config.load_config()
