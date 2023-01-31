from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath ="//*[@id='__next']/form/div/div[2]/button/span[1]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_pass(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_submit(self):
        self.click_on_the_element(self.sign_in_button_xpath)
    def page_title(self):
        assert self.get_page_title(self.login_url) == self.expected_title


