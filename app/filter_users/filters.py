import json
from sqlalchemy import func
from app.models import db, User, Department


def filter_by_offices(pk):
    employers = db.session.query(User, Department).filter(Department.office_id == pk).all()
    return employers


def filter_by_departments(pk):
    employers = db.session.query(User).filter(User.department_id == pk).all()
    return employers


def filter_by_roles(pk):
    employers = db.session.query(User).filter(User.role_id == pk).all()
    return employers


def filter_by_salary(salary):
    employers = db.session.query(User).filter(User.salary_user == salary).all()
    return employers


def filter_sum_salary_office(pk):
    employers = db.session.query(func.sum(User.salary_user), Department.office_id)\
        .filter(User.department_id == Department.id)\
        .filter(Department.office_id == pk)\
        .group_by(Department.office_id).all()
    print(employers)
    return employers


def json_dump(data):
    with open("app/json_requests/required_data.json", "w") as file:
        json.dump(data, file, indent=4)
