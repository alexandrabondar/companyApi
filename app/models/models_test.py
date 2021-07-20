from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from app import bcrypt, app
import datetime

Base = declarative_base()


class RoleTest(Base):

    __tablename__ = 'roles_test'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_role = Column(String(120), unique=True, nullable=False)
    users = relationship('UserTest', backref='roles_test', lazy=True)


class OfficeTest(Base):

    __tablename__ = 'offices_test'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), unique=True, nullable=False)
    address = Column(String(160))
    departments = relationship('DepartmentTest', backref='offices_test', lazy=True)


class DepartmentTest(Base):

    __tablename__ = 'departments_test'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), unique=True, nullable=False)
    office_id = Column(Integer, ForeignKey('offices_test.id'), nullable=False)
    users = relationship('UserTest', backref='departments_test', lazy=True)


class UserTest(Base):

    __tablename__ = "users_test"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    first_name_user = Column(String(80))
    last_name_user = Column(String(80))
    salary_user = Column(Float)
    created_at = Column(DateTime)
    role_id = Column(Integer, ForeignKey('roles_test.id'))
    department_id = Column(Integer, ForeignKey('departments_test.id'))

    def __init__(self, email, password, first_name_user, last_name_user, salary_user, department_id, role_id):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.first_name_user = first_name_user
        self.last_name_user = last_name_user
        self.salary_user = salary_user
        self.department_id = department_id
        self.role_id = role_id
        self.created_at = datetime.datetime.now()
