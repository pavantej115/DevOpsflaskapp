from app import app

def test_invalid_route_method():
    client = app.test_client()

    # Test POST request to /home (only GET is allowed)
    response = client.post("/home")
    assert response.status_code == 405
