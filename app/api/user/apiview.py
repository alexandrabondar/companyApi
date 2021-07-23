from flask import jsonify, request
from app import db
from app.models.models import User, UserSchema, Department
import json
from app.utils import session_add, session_delete, validate_data


def user_create(data):
    user = User.query.filter_by(email=data.get('email')).first()
    if not user:
        try:
            data = request.get_json()
            if any(validate_data(UserSchema(), data)):
                return {"status": "fail", "error": validate_data(UserSchema(), data)}
            else:
                user = User(email=data['email'], password=data['password'],
                            first_name_user=data['first_name_user'], last_name_user=data['last_name_user'],
                            salary_user=data['salary_user'], department_id=data['department_id'],
                            role_id=data['role_id'])
                session_add(user)
            auth_token = user.encode_auth_token(user.id)
            return jsonify({"auth_token": auth_token}), 201
        except Exception as e:
            print(e)
            return jsonify({"message": "invalid data"}), 400
    else:
        return jsonify({"message": "User is already exist"}), 401


def user_read():
    users = User.query.all()
    results = [
        {
            "id": user.id,
            "email": user.email,
            "first_name_user": user.first_name_user,
            "last_name_user": user.last_name_user,
            "salary_user": user.salary_user,
            "created_at": user.created_at,
            "role_id": user.role_id
        } for user in users
    ]
    return results


def user_read_by_pk(pk):
    user = User.query.get_or_404(pk)
    results = [
        {
            "id": user.id,
            "email": user.email,
            "first_name_user": user.first_name_user,
            "last_name_user": user.last_name_user,
            "salary_user": user.salary_user,
            "created_at": user.created_at,
            "role_id": user.role_id,
            "department_id": user.department_id
        }
    ]
    return results


def user_update_by_pk(pk):
    user = User.query.get_or_404(pk)
    data = request.get_json()
    for key, value in data.items():
        if key == 'email':
            user.email = data['email']
        elif key == 'first_name_user':
            user.first_name_user = data['first_name_user']
        elif key == 'last_name_user':
            user.last_name_user = data['last_name_user']
        elif key == 'department_id':
            user.department_id = data['department_id']
        elif key == 'role_id':
            user.role_id = data['role_id']
        elif key == 'salary_user':
            user.salary_user = data['salary_user']
        else:
            continue
    try:
        session_add(user)
    except Exception as e:
        print(e)
        return e


def user_delete_by_pk(pk):
    user = User.query.get_or_404(pk)
    session_delete(user)


def main_filter(*args):
    filters = args
    stmt = db.session.query(User, Department).filter(*filters)
    return stmt


def json_dump(data):
    with open("app/api/user/required_data.json", "w") as file:
        json.dump(data, file, indent=4)
