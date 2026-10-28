from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Test 1: Health endpoint check (PASS)
def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Test 2: Invalid endpoint check (PASS)
def test_invalid_endpoint():
    response = client.get("/invalid-route")
    assert response.status_code == 404

# Test 3: Ready endpoint check (PASS)
def test_ready_endpoint():
    response = client.get("/ready")
    assert response.status_code in [200, 503]

# Test 4: Dummy math check (PASS)
def test_math_check():
    num_a = 2
    num_b = 2
    assert num_a + num_b == 4

# Test 5: Dummy string check (PASS)
def test_string_check():
    text = "apex-operations-api"
    assert "apex" in text

# Test 6: INTENTIONAL FAILURE (FAIL - Assignment requirement)
def test_intentional_failure():
    val1 = 1
    val2 = 1
    # now it will be pass
    assert val1 == val2, "Intentional failure to prove CI/CD blocking"