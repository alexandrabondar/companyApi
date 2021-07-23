from flask import abort, Blueprint, session
from flask_jwt_extended import get_jwt_identity, jwt_required
from .apiview import *
from app import bcrypt
from app.permissions.permissions import head_company_or_office_required, head_company_required

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/create/', methods=['POST'])
@head_company_or_office_required()
def create():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            result = user_create(data)
            return result
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return abort(500)


@user_blueprint.route('/read/', methods=['GET'])
# @head_company_or_office_required()
def read():
    if request.method == 'GET':
        results = user_read()
        return jsonify({"users": results})
    else:
        return abort(500)


@user_blueprint.route('/read/<int:pk>/', methods=['GET'])
@head_company_or_office_required()
def read_one(pk):
    if request.method == 'GET':
        results = user_read_by_pk(pk)
        return jsonify({"user": results})
    else:
        return abort(500)


@user_blueprint.route('/read/me/', methods=['GET'])
@jwt_required()
def read_me():
    if request.method == 'GET':
        user = User.query.filter_by(id=get_jwt_identity()).first()
        results = user_read_by_pk(pk=user.id)
        return jsonify({"user": results})
    else:
        return abort(500)


@user_blueprint.route('/update/<int:pk>/', methods=['GET', 'PUT'])
@head_company_or_office_required()
def update(pk):
    if request.method == 'GET':
        results = user_read_by_pk(pk)
        return jsonify({"user": results}), 200
    elif request.method == 'PUT':
        user_update_by_pk(pk)
        return jsonify({"message": "user updated successfully"}), 200
    else:
        return abort(500)


@user_blueprint.route('/delete/<int:pk>', methods=['GET', 'DELETE'])
@head_company_or_office_required()
def delete(pk):
    if request.method == 'GET':
        results = user_read_by_pk(pk)
        return jsonify({"user": results}), 200
    elif request.method == 'DELETE':
        user_delete_by_pk(pk)
        return jsonify({"message": "user deleted successfully"}), 200
    else:
        return abort(500)


@user_blueprint.route('/login/', methods=['POST'])
def login_user():
    data = request.get_json()
    if request.method == 'POST':
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and bcrypt.check_password_hash(
                    user.password, data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    return jsonify({"auth_token": auth_token}), 200
                else:
                    return jsonify({'message': 'auth_token not created'}), 400
            else:
                return jsonify({'message': 'user does not exist'}), 400
        except Exception as e:
            print(e)
            return jsonify({'message': 'invalid data'}), 500
    else:
        abort(500)


@user_blueprint.route('/logout/', methods=['POST'])
def logout():
    if 'email' in session:
        session.pop('email', None)
    return jsonify({'message': 'You successfully logged out'})


@head_company_required()
@user_blueprint.route('/filter/', methods=['GET'])
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
