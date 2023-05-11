import json

def test_customer_index(app, client):
    response = client.get('/api/v1/customers', follow_redirects = True)
    assert response.status_code == 200
    assert len(response.json['customers']) == 2
    assert response.json['customers'][0]['name'] == 'John Doe'


def test_customer_create(app, client):
    payload = {"name":"Wilson Grey","dob":"2000-01-12","address":"Moritzplatz"}
    response = client.post(
        '/api/v1/customers',
        json = payload,
        headers = {"Content-Type": "application/json"},
        follow_redirects = True
    )
    assert response.status_code == 201
    assert response.json['name'] == 'Wilson Grey' and response.json['dob'] == '2000-01-12' and response.json['address'] == 'Moritzplatz'
    # expected = {"id":3,"name":"Wilson Grey","dob":"2000-01-12","address":"Moritzplatz"}
    # print(response.get_data(as_text=True))
    # assert expected == json.loads(response.get_data(as_text=True))


def test_customer_show(app, client):
    response = client.get('/api/v1/customers/1')
    assert response.status_code == 200
    assert response.json['id'] == 1
    assert response.json['name'] == 'John Doe'


def test_customer_update(app, client):
    payload = {"name":"John Doe","dob":"1990-01-01","address":"Beusselstraße"}
    response = client.patch(
        '/api/v1/customers/1',
        json = payload,
        headers = {"Content-Type": "application/json"},
        follow_redirects = True
    )
    assert response.status_code == 200
    assert response.json['name'] == 'John Doe' and response.json['dob'] == '1990-01-01' and response.json['address'] == 'Beusselstraße'


def test_customer_destroy(app, client):
    response = client.delete('/api/v1/customers/3')
    assert response.status_code == 204