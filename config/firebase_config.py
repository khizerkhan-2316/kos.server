import os

import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

cred_path = "key.json"

cred = credentials.Certificate(cred_path)

firebase_admin.initialize_app(cred)

db = firestore.client()

