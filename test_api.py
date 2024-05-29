import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_data_range():
    start_time = 0
    end_time = 10
    response = client.get(f"/data-range?start_time={start_time}&end_time={end_time}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
