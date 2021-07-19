from flask import Blueprint, abort, jsonify
from .apiview import *
from app.permissions.permissions import head_company_required

office_blueprint = Blueprint('office', __name__)


@office_blueprint.route('/create/', methods=['POST'])
@head_company_required()
def create():
    if request.method == 'POST':
        if request.is_json:
            office_create()
            return jsonify({"message": "Office has been created successfully"}), 200
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return abort(500)


@office_blueprint.route('/read/', methods=['GET'])
@head_company_required()
def read():
    if request.method == 'GET':
        results = office_read()
        return jsonify({"offices": results})
    else:
        return abort(500)


@office_blueprint.route('/read/<int:pk>/', methods=['GET'])
@head_company_required()
def read_one(pk):
    if request.method == 'GET':
        results = office_read_by_pk(pk)
        return jsonify({"office": results})
    else:
        return abort(500)


@office_blueprint.route('/update/<int:pk>/', methods=['GET', 'PUT'])
@head_company_required()
def update(pk):
    if request.method == 'GET':
        results = office_read_by_pk(pk)
        return jsonify({"office": results}), 200
    elif request.method == 'PUT':
        office_update_by_pk(pk)
        return jsonify({"message": "office updated successfully"}), 200
    else:
        return abort(500)


@office_blueprint.route('/delete/<int:pk>/', methods=['GET', 'DELETE'])
@head_company_required()
def delete(pk):
    if request.method == 'GET':
        results = office_read_by_pk(pk)
        return jsonify({"office": results}), 200
    elif request.method == 'DELETE':
        office_delete_by_pk(pk)
        return jsonify({"message": "office deleted successfully"}), 200
    else:
        return abort(500)





