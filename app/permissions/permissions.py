from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, current_user
from app.models.models import User
from app import jwt
SUPER_ADMIN = 1
HEAD_OF_COMPANY = 2
HEAD_OF_OFFICE = 3
STAFF = 4


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


def head_office_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if current_user.role_id == HEAD_OF_OFFICE:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Head of office only!"), 403
        return decorator
    return wrapper


def head_company_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if current_user.role_id == HEAD_OF_COMPANY or current_user.role_id == SUPER_ADMIN:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Head of company only!"), 403
        return decorator
    return wrapper


def head_company_or_office_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            role = current_user.role_id
            if role == HEAD_OF_COMPANY or role == HEAD_OF_OFFICE or role == SUPER_ADMIN:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Head of company or head of office only!"), 403
        return decorator
    return wrapper
