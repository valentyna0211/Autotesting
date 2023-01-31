from pages.base_page import BasePage
import time

class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'

    def page_title(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title