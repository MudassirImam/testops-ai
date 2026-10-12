import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health_endpoint_returns_success():
    response = requests.get(
        f"{BASE_URL}/health",
        timeout=5,
    )

    assert response.status_code == 200


def test_health_endpoint_returns_expected_payload():
    response = requests.get(
        f"{BASE_URL}/health",
        timeout=5,
    )

    assert response.json() == {"status": "ok"}