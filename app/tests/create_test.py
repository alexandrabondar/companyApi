import pytest
from sqlalchemy import create_engine
from ..models import models_test
from app.models.models_test import RoleTest, DepartmentTest, OfficeTest, UserTest
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.TestingConfig'
    )
app.config.from_object(app_settings)
db = SQLAlchemy(app)
db.init_app(app)


def test_case():
    assert app.config['DEBUG'] == True
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://root:root@localhost:5432/company_test'


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture(scope="session")
def connection():
    engine = create_engine(
        "postgresql://root:root@localhost:5432/company_test"
    )
    return engine.connect()


@pytest.fixture(scope="session")
def setup_database(connection):
    models_test.Base.metadata.bind = connection
    models_test.Base.metadata.create_all()

    yield

    models_test.Base.metadata.drop_all()


@pytest.fixture
def db_session(setup_database, connection):
    transaction = connection.begin()
    yield scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=connection)
    )
    transaction.commit()
    transaction.rollback()


def test_create_role(db_session):
    db_session.add(RoleTest(id=1, name_role="staff"))
    db_session.add(RoleTest(id=2, name_role="head_of_office"))
    db_session.add(RoleTest(id=3, name_role="head_of_company"))
    db_session.add(RoleTest(id=4, name_role="head_of_hr"))
    db_session.commit()


def test_create_office(db_session):
    db_session.add(OfficeTest(name="office_1", address="street_1"))
    db_session.commit()


def test_create_department(db_session):
    db_session.add(DepartmentTest(id=1, name="department_1", office_id=1))
    db_session.commit()


def test_create_user(db_session):
    db_session.add(
        UserTest(email="headofcompany@gmail.com", password="12345", first_name_user="Head", last_name_user="Company",
                 salary_user=100000, department_id=1, role_id=3))
    db_session.commit()
