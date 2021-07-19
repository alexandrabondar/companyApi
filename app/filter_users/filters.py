import json
from sqlalchemy import func
from app.models.models import db, User, Department


def main_filter(*args):
    filters = args
    stmt = db.session.query(User, Department).filter(*filters)
    return stmt


def filter_sum_salary_office(pk):
    employers = db.session.query(func.sum(User.salary_user), Department.office_id)\
        .filter(User.department_id == Department.id)\
        .filter(Department.office_id == pk)\
        .group_by(Department.office_id).all()
    print(employers)
    return employers


def json_dump(data):
    with open("app/filter_users/json_requests/required_data.json", "w") as file:
        json.dump(data, file, indent=4)
