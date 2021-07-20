import json
import pytest
from app import app
from app.tests.user_test import login_as_head_company
from app.api.office.apiview import office_read_by_pk


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client


def test_read(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_read = client.get('/office/read/',
                               headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_read.status_code == 200


def test_read_one(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_read = client.get('/office/read/1/',
                               headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    results = office_read_by_pk(1)
    mock_request_data = {'office': results}
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_read.json == mock_request_data
    assert response_read.status_code == 200


def test_update_by_pk(client):
    payload = login_as_head_company()
    response_login = client.post('/user/login/', headers={"Content-Type": "application/json"}, data=payload)
    data_login = json.loads(response_login.data)
    response_update = client.put('/office/update/1/', data=json.dumps(dict(name="Office1", address="Street1")),
                                 content_type='application/json',
                                 headers=dict(Authorization='Bearer ' + json.loads(response_login.data)['auth_token']))
    assert response_login.content_type == 'application/json'
    assert type(data_login['auth_token']) == str
    assert response_login.status_code == 200
    assert response_update.json == {'message': 'office updated successfully'}
    assert response_update.status_code == 200
