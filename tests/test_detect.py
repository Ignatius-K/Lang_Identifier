# import json
import json

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_welcome():
    response = client.get('/')
    assert response.json()['message'] == 'Hello world'
    assert response.status_code == 200


# @patch("model.model.Model", autospec=True)
def test_detect():
    content = {
        "text": "hello are you there"
    }

    response = client.post(
        url='/detect',
        content=json.dumps(content)
    )

    assert response.status_code == 200
    assert response.json()['lang'] == '0'
