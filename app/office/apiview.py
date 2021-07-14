from flask import request
from app import db
from app.models import Office


def office_create():
    name = request.json.get('name')
    address = request.json.get('address')
    new_office = Office(name=name, address=address)
    try:
        db.session.add(new_office)
        db.session.commit()
    except Exception as e:
        print(e)
        return e


def office_read():
    offices = Office.query.all()
    results = [
        {
            "id": office.id,
            "name": office.name,
            "address": office.address
        } for office in offices
    ]
    return results


def office_read_by_pk(pk):
    office = Office.query.get_or_404(pk)
    results = [
        {
            "id": office.id,
            "name": office.name,
            "address": office.address
        }
    ]
    return results


def office_update_by_pk(pk):
    office = Office.query.get_or_404(pk)
    data = request.get_json()
    office.name = data['name']
    office.address = data['address']
    try:
        db.session.add(office)
        db.session.commit()
    except Exception as e:
        print(e)
        return e


def office_delete_by_pk(pk):
    office = Office.query.get_or_404(pk)
    db.session.delete(office)
    db.session.commit()
