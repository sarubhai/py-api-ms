import json

def test_product_index(app, client):
    response = client.get('/api/v1/products', follow_redirects = True)
    assert response.status_code == 200
    assert len(response.json['products']) == 5
    assert response.json['products'][0]['name'] == 'Baseball Caps'


def test_product_create(app, client):
    payload = {"name":"Product1", "uom":"EA", "quantity":12, "price":10.50, "in_stock": True}
    response = client.post(
        '/api/v1/products',
        json = payload,
        headers = {"Content-Type": "application/json"},
        follow_redirects = True
    )
    assert response.status_code == 201
    assert response.json['product']['name'] == 'Product1' and response.json['product']['uom'] == 'EA' and response.json['product']['quantity'] == 12 and response.json['product']['price'] == 10.50 and response.json['product']['in_stock'] == True


def test_product_show(app, client):
    response = client.get('/api/v1/products/1')
    assert response.status_code == 200
    assert response.json['product']['id'] == 1
    assert response.json['product']['name'] == 'Baseball Caps'


def test_product_update(app, client):
    payload = {"name":"Baseball Caps", "uom":"Piece", "quantity":25, "price":10.99, "in_stock": True}
    response = client.patch(
        '/api/v1/products/1',
        json = payload,
        headers = {"Content-Type": "application/json"},
        follow_redirects = True
    )
    assert response.status_code == 200
    assert response.json['product']['name'] == 'Baseball Caps' and response.json['product']['uom'] == 'Piece' and response.json['product']['quantity'] == 25 and response.json['product']['price'] == 10.99 and response.json['product']['in_stock'] == True


def test_product_destroy(app, client):
    response = client.delete('/api/v1/products/3')
    assert response.status_code == 204