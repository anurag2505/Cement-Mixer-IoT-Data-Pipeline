import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.DATABASE_URL = os.getenv('DATABASE_URL')
        self.API_KEY = os.getenv('API_KEY')
        self.SECRET_KEY = os.getenv('SECRET_KEY')

    def get_database_url(self):
        return self.DATABASE_URL

    def get_api_key(self):
        return self.API_KEY

    def get_secret_key(self):
        return self.SECRET_KEY

config = Config()