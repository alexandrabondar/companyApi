from flask import abort, Blueprint
from .apiview import *
from ..permissions import head_company_required

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/create/', methods=['POST'])
@head_company_required()
def create():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            user_create(data)
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return abort(500)


@auth_blueprint.route('/read/', methods=['GET'])
@head_company_required()
def read():
    if request.method == 'GET':
        results = user_read()
        return jsonify({"users": results})
    else:
        return abort(500)


@auth_blueprint.route('/read/<int:pk>/', methods=['GET'])
@head_company_required()
def read_one(pk):
    if request.method == 'GET':
        results = user_read_by_pk(pk)
        return jsonify({"user": results})
    else:
        return abort(500)


@auth_blueprint.route('/update/<int:pk>/', methods=['GET', 'PUT'])
@head_company_required()
def update(pk):
    if request.method == 'GET':
        results = user_read_by_pk(pk)
        return jsonify({"user": results}), 200
    elif request.method == 'PUT':
        user_update_by_pk(pk)
        return jsonify({"message": "user updated successfully"}), 200
    else:
        return abort(500)


@auth_blueprint.route('/delete/<int:pk>', methods=['GET', 'DELETE'])
@head_company_required()
def delete(pk):
    if request.method == 'GET':
        results = user_read_by_pk(pk)
        return jsonify({"user": results}), 200
    elif request.method == 'DELETE':
        user_delete_by_pk(pk)
        return jsonify({"message": "user deleted successfully"}), 200
    else:
        return abort(500)


@auth_blueprint.route('/login/', methods=['GET'])
def login_user():
    data = request.get_json()
    if request.method == 'GET':
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and bcrypt.check_password_hash(
                    user.password, data.get('password')):
                # session['email'] = auth.email
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
