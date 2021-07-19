from flask import jsonify, Blueprint, abort
from .apiview import *
from app.permissions.permissions import head_company_required

role_blueprint = Blueprint('role', __name__)


@role_blueprint.route('/create/', methods=['POST'])
@head_company_required()
def create():
    if request.method == 'POST':
        if request.is_json:
            role_create()
            return jsonify({"message": "Role has been created successfully"})
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return abort(500)


@role_blueprint.route('/read/', methods=['GET'])
@head_company_required()
def read():
    if request.method == 'GET':
        results = role_read()
        return jsonify({"roles": results})
    else:
        return abort(500)


@role_blueprint.route('/read/<int:pk>/', methods=['GET'])
@head_company_required()
def read_one(pk):
    if request.method == 'GET':
        results = role_read_by_pk(pk)
        return jsonify({"role": results})
    else:
        return abort(500)


@role_blueprint.route('/update/<int:pk>/', methods=['GET', 'PUT'])
@head_company_required()
def update(pk):
    if request.method == 'GET':
        results = role_read_by_pk(pk)
        return jsonify({"role": results}), 200
    elif request.method == 'PUT':
        role_update_by_pk(pk)
        return jsonify({"message": "role updated successfully"}), 200
    else:
        return abort(500)


@role_blueprint.route('/delete/<int:pk>/', methods=['GET', 'DELETE'])
@head_company_required()
def delete(pk):
    if request.method == 'GET':
        results = role_read_by_pk(pk)
        return jsonify({"office": results}), 200
    elif request.method == 'DELETE':
        role_delete_by_pk(pk)
        return jsonify({"message": "role deleted successfully"}), 200
    else:
        return abort(500)
