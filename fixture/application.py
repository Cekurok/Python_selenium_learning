from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.webdriver = WebDriver("D:\driversWeb\chromedriver.exe")
        self.webdriver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.groups = GroupHelper(self)


    def open_home_page(self):
        webdriver = self.webdriver
        webdriver.get("http://localhost/addressbook/")
        webdriver.maximize_window()

    def destroy(self):
        self.webdriver.quit()