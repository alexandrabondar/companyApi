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

from app.api.user.views import user_blueprint
from app.api.office.views import office_blueprint
from app.api.department.views import department_blueprint
from app.api.role.views import role_blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(office_blueprint, url_prefix='/office')
app.register_blueprint(department_blueprint, url_prefix='/department')
app.register_blueprint(role_blueprint, url_prefix='/role')
