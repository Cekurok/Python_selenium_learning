import unittest as unittest
from selenium.webdriver.chrome.webdriver import WebDriver


def is_alert_present(wd):
    try:
        wd.switch_to_allert().txt
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.webdriver = WebDriver("D:\driversWeb\chromedriver.exe")
        self.webdriver.implicitly_wait(60)

    def test_test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(name="aqwe1", header="aqwe12", footer="aqwe123")
        self.return_groups_page()
        self.logout()

    def logout(self):
        webdriver = self.webdriver
        webdriver.find_element_by_link_text("Logout").click()

    def return_groups_page(self):
        webdriver = self.webdriver
        webdriver.find_element_by_link_text("group page").click()

    def create_group(self, name, header, footer):
        webdriver = self.webdriver
        # init group creation
        webdriver.find_element_by_name("new").click()
        # fill gpoup form
        webdriver.find_element_by_name("group_name").click()
        webdriver.find_element_by_name("group_name").clear()
        webdriver.find_element_by_name("group_name").send_keys(name)
        webdriver.find_element_by_name("group_header").click()
        webdriver.find_element_by_name("group_header").clear()
        webdriver.find_element_by_name("group_header").send_keys(header)
        webdriver.find_element_by_name("group_footer").click()
        webdriver.find_element_by_name("group_footer").clear()
        webdriver.find_element_by_name("group_footer").send_keys(footer)
        # submit to group cretion
        webdriver.find_element_by_name("submit").click()

    def open_group_page(self):
        webdriver = self.webdriver
        webdriver.find_element_by_link_text("groups").click()

    def login(self, username, password):
        webdriver = self.webdriver
        webdriver.find_element_by_name("user").click()
        webdriver.find_element_by_name("user").clear()
        webdriver.find_element_by_name("user").send_keys(username)
        webdriver.find_element_by_name("pass").click()
        webdriver.find_element_by_name("pass").clear()
        webdriver.find_element_by_name("pass").send_keys(password)
        webdriver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        webdriver = self.webdriver
        webdriver.get("http://localhost/addressbook/")
        webdriver.maximize_window()

    def tearDown(self):
        self.webdriver.quit()


if __name__ == '__main__':
    unittest.main()
