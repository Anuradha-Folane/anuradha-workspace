from pages.login_page import LoginPage

#login with correct credentials-Happy path scenario
def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in login_page.get_message()

#Login with incorrect credentials-Negative scenario
def test_valid_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("wronguser", "wrongpassword")

    assert "secure area" in login_page.get_message()
