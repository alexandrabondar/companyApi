from flask import request
from app.models.models import Department, DepartmentSchema
from app.utils import session_add, validate_data, session_delete


def department_create():
    data = request.get_json()
    if any(validate_data(DepartmentSchema(), data)):
        return {"status": "fail", "error": validate_data(DepartmentSchema(), data)}
    else:
        name = data['name']
        office_id = data['office_id']
        new_department = Department(name=name, office_id=office_id)
        try:
            session_add(new_department)
            return {"status": "success", "message": "Department has been created successfully"}
        except Exception as e:
            print(e)
            return {"status": "fail"}


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
    if any(validate_data(DepartmentSchema(), data)):
        return {"status": "fail", "error": validate_data(DepartmentSchema(), data)}
    else:
        department.name = data['name']
        department.office_id = data['office_id']
        try:
            session_add(department)
            return {"message": "department updated successfully"}
        except Exception as e:
            print(e)
            return {"status": "fail"}


def department_delete_by_pk(pk):
    department = Department.query.get_or_404(pk)
    session_delete(department)
