import os
from config import db
from models import Contact
from app import connex_app

CONTACTS = [
    {
        "id": 1,
        "nama": "Yogi",
        "noHp": "08123456789",
    },
    {
        "id": 2,
        "nama": "Faiz",
        "noHp": "081987654321",
    },
    {
        "id": 3,
        "nama": "Bahtiar",
        "noHp": "08454127844",
    },
]

# Delete database file if it exists currently
if os.path.exists('contacts'):
    os.remove('contacts')

# Create the database
with connex_app.app.app_context():
    db.create_all()

# Iterate over the PEOPLE structure and populate the database
    for contact in CONTACTS:
        p = Contact(id=contact['id'], nama=contact['nama'], noHp=contact['noHp'])
        db.session.add(p)

    db.session.commit()
