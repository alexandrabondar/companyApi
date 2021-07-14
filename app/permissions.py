from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, jwt_required, current_user
from .models import User
from app import jwt


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
            if current_user.role_id == 2:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Head of office only!"), 403
        return decorator
    return wrapper


def head_company_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if current_user.role_id == 3:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Head of company only!"), 403
        return decorator
    return wrapper


def staff_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            if current_user.role_id == 1:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Staff only!"), 403
        return decorator
    return wrapper
