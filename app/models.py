import datetime
from app import app, db, bcrypt
import jwt


class Office(db.Model):

    __tablename__ = 'offices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(160))
    departments = db.relationship('Department', backref='offices', lazy=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return self.name


class Department(db.Model):

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    office_id = db.Column(db.Integer, db.ForeignKey('offices.id'), nullable=False)
    users = db.relationship('User', backref='departments', lazy=True)

    def __init__(self, name, office_id):
        self.name = name
        self.office_id = office_id

    def __str__(self):
        return self.name


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name_user = db.Column(db.String(80))
    last_name_user = db.Column(db.String(80))
    salary_user = db.Column(db.Float)
    created_at = db.Column(db.DateTime, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __init__(self, email, password, first_name_user, last_name_user, salary_user, department_id, role_id):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.first_name_user = first_name_user
        self.last_name_user = last_name_user
        self.salary_user = salary_user
        self.role_id = role_id
        self.department_id = department_id
        self.created_at = datetime.datetime.now()

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=60),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e


class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_role = db.Column(db.String(120), unique=True, nullable=False)
    users = db.relationship('User', backref='Role', lazy=True)

    def __init__(self, name_role):
        self.name_role = name_role

    def __str__(self):
        return self.name_role
