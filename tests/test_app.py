import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def sample_data():
    """Fixture: retourne une liste d'exemples d'objets (simule des enregistrements).
    Réutilisable dans les tests nécessitant des données d'exemple."""
    return [
        {'id':1, 'url':'http://example.com/1', 'title': 'Example 1', 'author': 'Author 1'},
        {'id':2, 'url':'http://example.com/2', 'title': 'Example 2', 'author': 'Author 2'},
        {'id':3, 'url':'http://example.com/3', 'title': 'Example 3', 'author': 'Author 1'}
    ]


def test_videos_route(client, monkeypatch):


    #Replace utility.get_json par le mock_data
    monkeypatch.setattr("utility.get_json", lambda path: sample_data())

    #call route
    response = client.get('/videos')

    # Check http status
    assert response.status_code == 200
    data = response.data.decode("utf-8")

    # Check html
    assert "Example 1" in data
    assert "Example 2" in data
    assert "Example 3" in data

def test_video_details_ok(client, monkeypatch):

    #Replace utility.get_json par le mock_data
    monkeypatch.setattr("utility.get_json", lambda path: sample_data())

    #call route
    response = client.get('/get/video?id=1')

    # Check http status
    assert response.status_code == 200
    data = response.data.decode("utf-8")

    # Check html
    assert "Example 1" in data

def test_video_details_no_id(client, monkeypatch):



    #Replace utility.get_json par le sample_data
    monkeypatch.setattr("utility.get_json", lambda path: sample_data())

    #call route
    response = client.get('/get/video')

    # Check http status
    assert response.status_code == 400

def test_video_details_invalid_id(client, monkeypatch):


    #Replace utility.get_json par le sample_data
    monkeypatch.setattr("utility.get_json", lambda path: sample_data())

    #call route
    response = client.get('/get/video?id=4')

    # Check http status
    assert response.status_code == 404
