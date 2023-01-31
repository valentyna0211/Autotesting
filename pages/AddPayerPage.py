from pages.base_page import BasePage
from login_page import LoginPage
from dashboard import Dashboard
class Add_player_page(BasePage):
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    title = "Add player"
    Name_field_xpath = "//input[@name='name']"
    Surname_field_xpath = "//input[@name='surname']"
    Main_position_xpath = "//input[@name='mainPosition']"
    age_xpath = "//input[@name='age']"
    submit_button = "//button[@type='submit']"
    clear_button = "//button[@type='submit']"


    def type_in_name(self, name):
        self.field_send_keys(self.Name_field_xpath, name)

    def type_in_surname(self,surname):
        self.field_send_keys(self.Surname_field_xpath,surname)

    def type_in_main_position(self, position):
            self.field_send_keys(self.Main_position_xpath, position)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def click_on_submit(self):
        self.click_on_the_element(self.submit_button )
    def page_title(self):
        assert self.get_page_title(self.add_player_url) == self.title



