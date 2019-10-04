from firebase_admin import firestore, credentials

cred = credentials.Certificate("config/s.key")
firebase_admin.initialize_app(cred)
db = firestore.client()

if db = None:
    else:
        db = firestore

def createProfile():
    pass

