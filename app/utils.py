from app import db


def session_add(instance):
    db.session.add(instance)
    db.session.commit()


def session_delete(instance):
    db.session.delete(instance)
    db.session.commit()


def validate_data(instance, data):
    errors = instance.validate(data)
    return errors
