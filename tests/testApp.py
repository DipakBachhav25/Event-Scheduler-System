# tests/testApp.py

import pytest
from event_app import app, load_events, DATA_FILE
import json
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def clear_data_file():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_create_event(client):
    response = client.post('/events', json={
        "title": "Test Event",
        "description": "This is a test event",
        "start_time": "2025-04-05T10:00:00",
        "end_time": "2025-04-05T11:00:00"
    })
    assert response.status_code == 201

def test_search_by_title(client):
    client.post('/events', json={
        "title": "Team Meeting",
        "description": "Weekly team sync",
        "start_time": "2025-04-05T09:00:00",
        "end_time": "2025-04-05T10:00:00"
    })

    client.post('/events', json={
        "title": "Lunch Break",
        "description": "Casual lunch",
        "start_time": "2025-04-05T12:00:00",
        "end_time": "2025-04-05T13:00:00"
    })

    response = client.get('/search?q=team')
    data = response.get_json()

    assert len(data) == 1
    assert data[0]['title'] == "Team Meeting"

def test_search_by_description(client):
    client.post('/events', json={
        "title": "Morning Coffee",
        "description": "Daily coffee with team",
        "start_time": "2025-04-06T08:00:00",
        "end_time": "2025-04-06T08:30:00"
    })

    response = client.get('/search?q=coffee')
    data = response.get_json()

    assert len(data) == 1
    assert data[0]['description'] == "Daily coffee with team"

def test_search_case_insensitive(client):
    client.post('/events', json={
        "title": "Important Conference",
        "description": "Annual tech conference",
        "start_time": "2025-04-10T10:00:00",
        "end_time": "2025-04-10T12:00:00"
    })

    response = client.get('/search?q=CONFERENCE')
    data = response.get_json()

    assert len(data) == 1
    assert data[0]['title'] == "Important Conference"

def test_search_no_match(client):
    response = client.get('/search?q=nonexistent')
    data = response.get_json()
    assert len(data) == 0