from library.basics_selenium_actions import *
from library.comparision_actions import *
from library.exception_handlers import *
from constants.xpath.saucedemo import *
from library.data_helper import *
import pytest
import time

@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_login(self):
        data = read_csv_data("/Users/chiranth.c/Documents/selenium_framework/constants/data/saus_demo_login.csv")
        wait_until_element_is_visible(self.driver, txt_box_username)
        enter_text_in_element(self.driver, txt_box_username, data[0]['txt_box_username'])
        enter_text_in_element(self.driver, txt_box_password, data[0]['txt_box_password'])
        click_element(self.driver, btn_login)
        take_screenshot(self.driver,"test_pytest_1.png")
