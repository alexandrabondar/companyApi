from flask.cli import FlaskGroup
from app import app, db
from app.models import models
from app.utils import session_add
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("create_superuser")
def create_superuser():
    office = models.Office(name="Office_1", address="Street_1")
    session_add(office)
    department = models.Department(name="Department_1", office_id=1)
    session_add(department)
    role_admin = models.Role(name_role="super_admin")
    session_add(role_admin)
    role_head_of_company = models.Role(name_role="head_of_company")
    session_add(role_head_of_company)
    role_head_of_office = models.Role(name_role="head_of_office")
    session_add(role_head_of_office)
    role_staff = models.Role(name_role="staff")
    session_add(role_staff)
    user = models.User(email="super_admin@gmail.com", password="12345",
                       first_name_user="Super", last_name_user="Admin",
                       salary_user=99999, department_id=1, role_id=1)
    session_add(user)


if __name__ == "__main__":
    cli()
