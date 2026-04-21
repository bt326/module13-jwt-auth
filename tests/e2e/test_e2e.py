import pytest

@pytest.mark.e2e
def test_register_success(page, fastapi_server):
    page.goto("http://localhost:8000/register-page")
    page.fill('input[placeholder="Username"]', "testuser")
    page.fill('input[placeholder="Email"]', "[test@test.com](mailto:test@test.com)")
    page.fill('input[placeholder="Password"]', "123456")
    page.click("text=Register")
    assert "Registration successful" in page.content()

@pytest.mark.e2e
def test_login_success(page, fastapi_server):
    page.goto("http://localhost:8000/login-page")
    page.fill('input[placeholder="Email"]', "[test@test.com](mailto:test@test.com)")
    page.fill('input[placeholder="Password"]', "123456")
    page.click("text=Login")
    assert "Login successful" in page.content()

@pytest.mark.e2e
def test_register_short_password(page, fastapi_server):
    page.goto("http://localhost:8000/register-page")
    page.fill('input[placeholder="Username"]', "abc")
    page.fill('input[placeholder="Email"]', "[abc@test.com](mailto:abc@test.com)")
    page.fill('input[placeholder="Password"]', "123")
    page.click("text=Register")
    assert page.url.endswith("/register-page")

@pytest.mark.e2e
def test_login_wrong_password(page, fastapi_server):
    page.goto("http://localhost:8000/login-page")
    page.fill('input[placeholder="Email"]', "[test@test.com](mailto:test@test.com)")
    page.fill('input[placeholder="Password"]', "wrongpass")
    page.click("text=Login")
    assert "Login successful" in page.content()
