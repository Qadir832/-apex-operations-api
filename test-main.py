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
    # Ready test passes if it connects or gracefully fails
    assert response.status_code in [200, 503]

# Test 4: Dummy math check (PASS)
def test_math_check():
    assert 2 + 2 == 4

# Test 5: Dummy string check (PASS)
def test_string_check():
    assert "apex" in "apex-operations-api"

# Test 6: INTENTIONAL FAILURE (FAIL - Assignment requirement)
def test_intentional_failure():
    # Yeh test jaan bujh kar fail hoga taake CI/CD pipeline ruk jaye
    assert 1 == 2, "Intentional failure to prove CI/CD blocks deployment"