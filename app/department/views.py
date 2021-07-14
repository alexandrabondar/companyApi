from flask import Blueprint, abort, jsonify
from .apiview import *

department_blueprint = Blueprint('department', __name__)


@department_blueprint.route('/create/', methods=['POST'])
def create():
    if request.method == 'POST':
        if request.is_json:
            department_create()
            return f'Department has been created successfully'
        else:
            return jsonify({"error": "The request payload is not in JSON format"})
    else:
        return abort(500)


@department_blueprint.route('/read/', methods=['GET'])
def read():
    if request.method == 'GET':
        results = department_read()
        return jsonify({"departments": results})
    else:
        return abort(500)


@department_blueprint.route('/read/<int:pk>/', methods=['GET'])
def read_one(pk):
    if request.method == 'GET':
        results = department_read_by_pk(pk)
        return jsonify({"department": results})
    else:
        return abort(500)


@department_blueprint.route('/update/<int:pk>/', methods=['GET', 'PUT'])
def update(pk):
    if request.method == 'GET':
        results = department_read_by_pk(pk)
        return jsonify({"department": results}), 200
    elif request.method == 'PUT':
        department_update_by_pk(pk)
        return jsonify({"message": "department updated successfully"}), 200
    else:
        return abort(500)


@department_blueprint.route('/delete/<int:pk>/', methods=['GET', 'DELETE'])
def delete(pk):
    if request.method == 'GET':
        results = department_read_by_pk(pk)
        return jsonify({"department": results}), 200
    elif request.method == 'DELETE':
        department_delete_by_pk(pk)
        return jsonify({"message": "department deleted successfully"}), 200
    else:
        return abort(500)
