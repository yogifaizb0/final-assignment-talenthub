from flask import make_response, abort
from config import db
from models import Contact, ContactSchema


def read_all():
    contact = Contact.query.order_by(Contact.id).all()

    contact_schema = ContactSchema(many=True)
    data = contact_schema.dump(contact)
    return data


def create(contact):
    nama = contact.get("nama")
    noHp = contact.get("noHp")

    existing_contact = (
        Contact.query.filter(Contact.nama == nama)
        .filter(Contact.noHp == noHp)
        .one_or_none()
    )

    if existing_contact is None:
        schema = ContactSchema()
        new_contact = Contact(nama = nama, noHp = noHp)

        db.session.add(new_contact)
        db.session.commit()

        data = schema.dump(new_contact)

        return data, 201
    
    else:
        abort (
            409, 
            "Orang dengan {nama} sudah ada".format(
                nama=nama, noHp=noHp
            ),
        )


def read_one(id):
    contact = Contact.query.filter(Contact.id == id).one_or_none()

    if contact is not None:
        contact_schema = ContactSchema()
        data = contact_schema.dump(contact)
        return data
    
    else:
        abort (
            404,
            "Contact dengan Id {id} tidak ditemukan".format(id=id),
        )

def update(id, contact):
    update_contact = Contact.query.filter(
        Contact.id == id
    ).one_or_none()

    nama = contact.get("nama")
    noHp = contact.get("noHp")

    existing_contact = (
        Contact.query.filter(Contact.nama == nama)
        .filter(Contact.noHp == noHp)
        .one_or_none()
    )

    if update_contact is None:
        abort(
            404,
            "Contact dengan Id {id} tidak ditemukan".format(id=id),
        )

    elif (existing_contact is not None and existing_contact.id != id):
        abort (
            409,
            "Contact dengan nama {nama} sudah ada".format(
                nama=nama  
            ),
        )

    else: 
        schema = ContactSchema()
        updated_contact = Contact(nama=nama, noHp=noHp, id=id)

        db.session.merge(updated_contact)
        db.session.commit()

        data = schema.dump(update_contact)

        return data, 200
    

def delete(id):
    contact = Contact.query.filter(Contact.id == id).one_or_none()

    if contact is not None:
        db.session.delete(contact)
        db.session.commit()
        return make_response(
            "Contact dengan id {id} sudah di hapus".format(id=id), 200
        )
    
    else:
        abort(
            404,
            "Contact dengan Id {id} tidak ditemukan".format(id=id),
        )