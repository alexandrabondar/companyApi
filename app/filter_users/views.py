from flask import Blueprint, jsonify, request
from app.permissions.permissions import head_company_required
from app.filter_users.filters import *


filter_blueprint = Blueprint('filter', __name__)

# JSON request example
# {
#     "department_id": 1,
#     "salary_user": 2300,
#     "office_id": 1
# }


@head_company_required()
@filter_blueprint.route('/', methods=['GET'])
def filter_by_params():
    filters = []
    data = request.get_json()
    for key, value in data.items():
        if key == "office_id":
            filters.append(getattr(Department, key) == value)
        elif key == "department_id":
            filters.append(getattr(User, key) == value)
        elif key == "salary_user":
            filters.append(getattr(User, key) == value)
        elif key == "role_id":
            filters.append(getattr(User, key) == value)

    filtered_users = main_filter(*filters)
    results = [{
        "id": filtered_user[0].id,
        "first_name_user": filtered_user[0].first_name_user,
        "last_name_user": filtered_user[0].last_name_user,
        "role_id": filtered_user[0].role_id,
        "salary_user": filtered_user[0].salary_user,
        "department_id": filtered_user[0].department_id,
        "office_id": filtered_user[1].office_id
    } for filtered_user in filtered_users]
    json_dump(results)
    return jsonify({"result": results})


@filter_blueprint.route('/salary/office/<int:pk>/', methods=['GET'])
@head_company_required()
def filter_sum_salary_by_office(pk):
    filter_data = filter_sum_salary_office(pk)
    salary, office_id = filter_data[0]
    results = [
        {
            "sum_salary": salary,
            "office_id": office_id,
         }]
    return jsonify({"result": results})
