class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#username"
        self.password = "#password"
        self.login_button = "button[type='submit']"
        self.flash_message = "#flash"

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)

    def get_message(self):
        return self.page.inner_text(self.flash_message)