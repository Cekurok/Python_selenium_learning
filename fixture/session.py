
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        webdriver = self.app.webdriver
        self.app.open_home_page()
        webdriver.find_element_by_name("user").click()
        webdriver.find_element_by_name("user").clear()
        webdriver.find_element_by_name("user").send_keys(username)
        webdriver.find_element_by_name("pass").click()
        webdriver.find_element_by_name("pass").clear()
        webdriver.find_element_by_name("pass").send_keys(password)
        webdriver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        webdriver = self.app.webdriver
        webdriver.find_element_by_link_text("Logout").click()