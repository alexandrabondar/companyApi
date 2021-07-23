from flask import request
from app import db
from app.models.models import Office, OfficeSchema, User, Department
from sqlalchemy import func
from app.utils import session_add, session_delete, validate_data


def office_create():
    data = request.get_json()
    if any(validate_data(OfficeSchema(), data)):
        return {"status": "fail", "error": validate_data(OfficeSchema(), data)}
    else:
        name = data['name']
        address = data['address']
        new_office = Office(name=name, address=address)
        try:
            session_add(new_office)
            return {"status": "success", "message": "Office has been created successfully"}
        except Exception as e:
            print(e)
            return {"status": "fail"}


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
    if any(validate_data(OfficeSchema(), data)):
        return {"status": "fail", "error": validate_data(OfficeSchema(), data)}
    else:
        office.name = data['name']
        office.address = data['address']
        try:
            session_add(office)
            return {"status": "success", "message": "Office has been update successfully"}
        except Exception as e:
            print(e)
            return {"status": "fail"}


def office_delete_by_pk(pk):
    office = Office.query.get_or_404(pk)
    session_delete(office)


def filter_sum_salary_office(pk):
    employers = db.session.query(func.sum(User.salary_user), Department.office_id)\
        .filter(User.department_id == Department.id)\
        .filter(Department.office_id == pk)\
        .group_by(Department.office_id).all()
    print(employers)
    return employers
