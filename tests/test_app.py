from fastapi.testclient import TestClient
from fast_api.app import app 

client = TestClient(app)

def test_read_main():
    response = client.get("/home")
    assert "text/html" in response.headers["content-type"]
    assert response.status_code == 200
    assert "<h1>Hello World</h1>" in response.text







    #fastapi dev fast_api/app.py --host 0.0.0.0