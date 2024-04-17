import os

firebase_credentials_path = os.getenv('FIREBASE_CREDENTIALS_PATH')

FIREBASE_CONFIG = {
    'credentials_path': firebase_credentials_path
}