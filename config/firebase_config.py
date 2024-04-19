import os

import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

current_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(current_dir, 'key.json')

cred = credentials.Certificate(key_path)

firebase_admin.initialize_app(cred)

db = firestore.client()

