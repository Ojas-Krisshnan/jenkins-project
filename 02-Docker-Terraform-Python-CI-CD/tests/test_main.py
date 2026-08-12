import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["docs_url"] == "/docs"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data

def test_get_items():
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["name"] == "Initial DevOps Workflow"

def test_get_single_item():
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Initial DevOps Workflow"

def test_get_nonexistent_item():
    response = client.get("/api/v1/items/9999")
    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()

def test_create_item():
    payload = {
        "name": "Docker Container Test",
        "description": "Integration testing for containerized app",
        "category": "testing"
    }
    response = client.post("/api/v1/items", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["description"] == payload["description"]
    assert "id" in data
    assert "created_at" in data

def test_delete_item():
    # First create an item to delete
    create_resp = client.post("/api/v1/items", json={"name": "Temp Item", "category": "temp"})
    item_id = create_resp.json()["id"]

    # Delete it
    del_resp = client.delete(f"/api/v1/items/{item_id}")
    assert del_resp.status_code == 204

    # Verify it is gone
    get_resp = client.get(f"/api/v1/items/{item_id}")
    assert get_resp.status_code == 404

def test_metrics_endpoint():
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    data = response.json()
    assert data["uptime_status"] == "UP"
    assert "total_items" in data
    assert data["system_info"]["python_framework"] == "FastAPI"
