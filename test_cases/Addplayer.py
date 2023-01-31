import os
import time
import unittest
from selenium import webdriver

from test_cases import login
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.AddPayerPage import Add_player_page


class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_login(self):
        user_login = LoginPage(self.driver)
        user_login.get_page_title()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_pass('Test-1234')
        user_login.click_on_submit()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.page_title()
        #time.sleep(5)

    def test_add_player(self):
        test_cases.TestLogin()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        add_player = Add_player_page(self.driver)
        add_player.page_title()
        add_player.type_in_name('Valentyna')
        add_player.type_in_surname('Malakhova')
        add_player.type_in_main_position('quarterback')
        add_player.type_in_age('19920211')
        add_player.click_on_submit()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")





