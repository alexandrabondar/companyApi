import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
    )
app.config.from_object(app_settings)
jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

from app.auth.views import auth_blueprint
from app.office.views import office_blueprint
from app.department.views import department_blueprint
from app.role.views import role_blueprint
from .filter_users.views import filter_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(office_blueprint, url_prefix='/office')
app.register_blueprint(department_blueprint, url_prefix='/department')
app.register_blueprint(role_blueprint, url_prefix='/role')
app.register_blueprint(filter_blueprint, url_prefix='/filter')
