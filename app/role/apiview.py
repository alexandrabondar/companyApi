from flask import request
from app import db
from app.models import Role


def role_create():
    name_role = request.json.get('name_role')
    new_role = Role(name_role=name_role)
    try:
        db.session.add(new_role)
        db.session.commit()
    except Exception as e:
        print(e)
        return e


def role_read():
    roles = Role.query.all()
    results = [
        {
            "id": role.id,
            "name_role": role.name_role
        } for role in roles
    ]
    return results


def role_read_by_pk(pk):
    role = Role.query.get_or_404(pk)
    results = [
        {
            "id": role.id,
            "name_role": role.name_role
        }
    ]
    return results


def role_update_by_pk(pk):
    role = Role.query.get_or_404(pk)
    data = request.get_json()
    role.name_role = data['name_role']
    try:
        db.session.add(role)
        db.session.commit()
    except Exception as e:
        print(e)
        return e


def role_delete_by_pk(pk):
    role = Role.query.get_or_404(pk)
    db.session.delete(role)
    db.session.commit()