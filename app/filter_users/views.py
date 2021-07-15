from flask import Blueprint, jsonify
from ..permissions import head_company_required
from ..filter_users.filters import *

filter_blueprint = Blueprint('filter', __name__)


@filter_blueprint.route('/office/<int:pk>/', methods=['GET'])
def filter_office(pk):
    filtered_users = filter_by_offices(pk)
    results = [
        {
            "id": filtered_user[0].id,
            "first_name_user": filtered_user[0].first_name_user,
            "last_name_user": filtered_user[0].last_name_user,
            "office_id": filtered_user[1].office_id
        } for filtered_user in filtered_users]
    json_dump(results)
    return jsonify({"result": results})


@filter_blueprint.route('/department/<int:pk>/', methods=['GET'])
def filter_department(pk):
    filtered_users = filter_by_departments(pk)
    results = [
        {
            "id": filtered_user.id,
            "first_name_user": filtered_user.first_name_user,
            "last_name_user": filtered_user.last_name_user,
            "department_id": filtered_user.department_id
        } for filtered_user in filtered_users]
    json_dump(results)
    return jsonify({"result": results})


@filter_blueprint.route('/role/<int:pk>/', methods=['GET'])
def filter_role(pk):
    filtered_users = filter_by_roles(pk)
    results = [
        {
            "id": filtered_user.id,
            "first_name_user": filtered_user.first_name_user,
            "last_name_user": filtered_user.last_name_user,
            "role_id": filtered_user.role_id
        } for filtered_user in filtered_users]
    json_dump(results)
    return jsonify({"result": results})


@filter_blueprint.route('/salary/<int:salary>/', methods=['GET'])
def filter_salary(salary):
    filtered_users = filter_by_salary(salary)
    results = [
        {
            "id": filtered_user.id,
            "first_name_user": filtered_user.first_name_user,
            "last_name_user": filtered_user.last_name_user,
            "salary_user": filtered_user.salary_user
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

