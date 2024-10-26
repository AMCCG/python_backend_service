from app.util.util_constant import Constant
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get(Constant.ROOT_PATH + "/greeting")
    assert response.status_code == 200
    assert response.json() == {
        "greeting": "Hello World Python",
        "hostname": "http://127.0.0.1:8000",
        "version": "v12"
    }
