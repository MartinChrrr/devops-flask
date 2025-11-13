import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client



def test_videos_route(client, monkeypatch):
    # Data so we don't read json
    mock_data = [
        {"id": 1, "title": "Test Video", "url": "https://x", "views": 5},
        {"id": 2, "title": "Autre Video", "url": "https://y", "views": 7},
    ]

    #Replace utility.get_json par le mock_data
    monkeypatch.setattr("utility.get_json", lambda path: mock_data)

   #call road
    response = client.get('/videos')

    # Check http status
    assert response.status_code == 200
    data = response.data.decode("utf-8")

    # Check html
    assert "Test Video" in data
    assert "Autre Video" in data

def test_video(client, monkeypatch):
    # Data so we don't read json
    mock_data = [
        {"id": 1, "title": "Test Video", "url": "https://x", "views": 5},
        {"id": 2, "title": "Autre Video", "url": "https://y", "views": 7},
    ]

    #Replace utility.get_json par le mock_data
    monkeypatch.setattr("utility.get_json", lambda path: mock_data)

       #call road
    response = client.get('/get/video?id=1')

    # Check http status
    assert response.status_code == 200
    data = response.data.decode("utf-8")

    # Check html
    assert "Test Video" in data
