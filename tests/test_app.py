from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from fast_api.app import app 

@pytest.fixture
def client():
    return TestClient(app)
'''    
def test_read_root(client):
   #Arrange(organizacao)
    response = client.get('/') #cliente requisita o / #act(Acao)

    assert response.status_code == 200 #assert(afirma)
    assert response.json() == {'message': 'ola mundo'}
        


def test_read_home():
    client = TestClient(app)
    response = client.get("/home")
    assert "text/html" in response.headers["content-type"]
    assert response.status_code == 200
    assert "<h1>Hello World</h1>" in response.text
''' 
def test_criar_usuario():
    client = TestClient(app)
    response = client.post(
        '/usuario',
        json={
            'nome_de_usuario': 'chico',
            'email': 'chico@exemplo.com',
            'senha': 'seguro',
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        
        'email': 'chico@exemplo.com',
        'nome_de_usuario': 'chico',
        'id':1
    }
def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    json1= {
        'users': [
            {
                'nome_de_usuario': 'chico',
                'email': 'chico@exemplo.com',
                'id': 1,
            }
        ]
    }
    assert response.json() == json1

def test_update_user(client):
    response = client.put(
        '/users/1',
        json= {
            'nome_de_usuario': 'chico',
            'email': 'chico@exemplo.com',
            "senha": "string123",
        }
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
                'nome_de_usuario': 'chico',
                'email': 'chico@exemplo.com',
                'id': 1
        }
    #fastapi dev fast_api/app.py --host 0.0.0.0
def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {
                'nome_de_usuario': 'chico',
                'email': 'chico@exemplo.com',
                'id': 1
        }