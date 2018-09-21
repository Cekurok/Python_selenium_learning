
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_groups_page(self):
        webdriver = self.app.webdriver
        webdriver.find_element_by_link_text("group page").click()

    def create(self, group):
        webdriver = self.app.webdriver
        self.open_group_page()
        # init group creation
        webdriver.find_element_by_name("new").click()
        # fill gpoup form
        webdriver.find_element_by_name("group_name").click()
        webdriver.find_element_by_name("group_name").clear()
        webdriver.find_element_by_name("group_name").send_keys(group.name)
        webdriver.find_element_by_name("group_header").click()
        webdriver.find_element_by_name("group_header").clear()
        webdriver.find_element_by_name("group_header").send_keys(group.header)
        webdriver.find_element_by_name("group_footer").click()
        webdriver.find_element_by_name("group_footer").clear()
        webdriver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit to group cretion
        webdriver.find_element_by_name("submit").click()
        self.return_groups_page()

    def open_group_page(self):
        webdriver = self.app.webdriver
        webdriver.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        webdriver = self.app.webdriver
        self.open_group_page()
        # select first group
        webdriver.find_element_by_name("selected[]").click()
        # delete first group
        webdriver.find_element_by_name("delete").click()
        self.return_groups_page()
