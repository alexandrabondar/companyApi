import json
import pytest
from app import app
from app.tests.user_test import login_as_head_company
from app.api.department.apiview import department_read_by_pk, department_update_by_pk


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client


def test_login(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    assert response_login.content_type == 'application/json'


def test_read(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_read = client.get('/department/read/',
                               headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_read.status_code == 200


def test_read_one(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_read = client.get('/department/read/1/',
                               headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    results = department_read_by_pk(1)
    mock_request_data = {'department': results}
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_read.json == mock_request_data
    assert response_read.status_code == 200


def test_update_by_pk(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_update = client.put('/department/update/1/', data = json.dumps(dict(name="Department1",office_id=1)),
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_update.json == {'message': 'department updated successfully'}
    assert response_update.status_code == 200
