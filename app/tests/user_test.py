import json
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client


def login_as_staff():
    payload = json.dumps({
        "email": 'miniflatalex@gmail.com',
        "password": '12345'
    })
    return payload


def login_as_head_company():
    payload = json.dumps({
        "email": "headofcompany@gmail.com",
        "password": "12345"
    })
    return payload


def test_login(client):
    payload = login_as_staff()
    response = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response.data)
    assert response.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response.status_code == 200


def test_read(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_read = client.get('/user/read/',
                               headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_read.status_code == 200


def test_read_one(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_read = client.get('/user/read/1/',
                               headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    mock_request_data = {"user": [
        {
            "created_at": "Thu, 08 Jul 2021 17:07:08 GMT",
            "department_id": 1,
            "email": "arturpirozhkov@gmail.com",
            "first_name_user": "Mifodiy",
            "id": 1,
            "last_name_user": "Pirozhkov",
            "role_id": 1,
            "salary_user": 2300.0}]}
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_read.json == mock_request_data
    assert response_read.status_code == 200


def test_update_by_pk(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_update = client.put('/user/update/1/', data=json.dumps(dict(first_name_user="Mifodiy")),
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_update.json == {'message': 'user updated successfully'}
    assert response_update.status_code == 200
