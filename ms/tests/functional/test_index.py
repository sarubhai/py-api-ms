import json

def test_health(app, client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    assert response.json['message'] == 'server up!'

def test_hotreload(app, client):
    response = client.get('/api/v1/hotreload')
    assert response.status_code == 200
    assert response.json['message'] == 'Test Hot Reload by changing this message!'