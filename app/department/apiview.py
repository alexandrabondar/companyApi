from flask import request
from app import db
from app.models import Department


def department_create():
    name = request.json.get('name')
    office_id = request.json.get('office_id')
    new_department = Department(name=name, office_id=office_id)
    try:
        db.session.add(new_department)
        db.session.commit()
    except Exception as e:
        print(e)
        return e


def department_read():
    departments = Department.query.all()
    results = [
        {
            "id": department.id,
            "name": department.name,
            "office_id": department.office_id
        } for department in departments
    ]
    return results


def department_read_by_pk(pk):
    department = Department.query.get_or_404(pk)
    results = [
        {
            "id": department.id,
            "name": department.name,
            "office_id": department.office_id
        }
    ]
    return results


def department_update_by_pk(pk):
    department = Department.query.get_or_404(pk)
    data = request.get_json()
    department.name = data['name']
    department.office_id = data['office_id']
    try:
        db.session.add(department)
        db.session.commit()
    except Exception as e:
        print(e)
        return e


def department_delete_by_pk(pk):
    department = Department.query.get_or_404(pk)
    db.session.delete(department)
    db.session.commit()

