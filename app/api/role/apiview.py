from flask import request
from app.models.models import Role, RoleSchema
from app.utils import session_add, session_delete, validate_data


def role_create():
    data = request.get_json()
    if any(validate_data(RoleSchema(), data)):
        return {"status": "fail", "error": validate_data(RoleSchema(), data)}
    else:
        name_role = data['name_role']
        new_role = Role(name_role=name_role)
        try:
            session_add(new_role)
            return {"status": "success", "message": "Role has been created successfully"}
        except Exception as e:
            print(e)
            return {"status": "fail"}


def role_read():
    roles = Role.query.all()
    results = [
        {
            "id": role.id,
            "name_role": role.name_role
        } for role in roles
    ]
    return results


def role_read_by_pk(pk):
    role = Role.query.get_or_404(pk)
    results = [
        {
            "id": role.id,
            "name_role": role.name_role
        }
    ]
    return results


def role_update_by_pk(pk):
    role = Role.query.get_or_404(pk)
    data = request.get_json()
    if any(validate_data(RoleSchema(), data)):
        return {"status": "fail", "error": validate_data(RoleSchema(), data)}
    else:
        role.name_role = data['name_role']
        try:
            session_add(role)
            return {"status": "success", "message": "Role has been update successfully"}
        except Exception as e:
            print(e)
            return {"status": "fail"}


def role_delete_by_pk(pk):
    role = Role.query.get_or_404(pk)
    session_delete(role)
