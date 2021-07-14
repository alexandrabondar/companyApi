import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = "/xb7/x11/x08h/x959Y/xd7/rz/x94{~/xe5/x80e/xed/xfa/x86/xd7$/x86/xaa0"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # \xb7\x11\x08h\x959Y\xd7\rz\x94{~\xe5\x80e\xed\xfa\x86\xd7$\x86\xaa0
    # app.config['SECRET_KEY'] = secret_key


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@localhost:5432/test_test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# class TestingConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://root:root@localhost:5432/test_test_db')


# app = Flask(__name__)
# bcrypt = Bcrypt(app)
# app.register_blueprint(auth, url_prefix='/auth')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost:5432/test_test_db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
