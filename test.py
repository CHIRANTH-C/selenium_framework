# from basics_functions import open_browser_to_link , click_element, enter_text_in_element,get_element_text,scroll_element_into_view,select_value_in_dropdown

# from basics_functions import *

from library.basics_selenium_actions import *
from constants.xpath.art_of_testing import *
from library.comparision_actions import *
from library.exception_handlers import *
from constants.xpath.sauce_demo import *
from constants.xpath.saucedemo import *
from library.video_recorder import recording
import time
from library.data_helper import *
import multiprocessing

def main():
    recording_process = multiprocessing.Process(target=recording)
    recording_process.start()

    data = read_csv_data("/Users/chiranth.c/Documents/selenium_framework/constants/data/saus_demo_login.csv")
    driver = open_browser("https://www.saucedemo.com/")
    """
    wait_until_element_is_visible(driver, txt_box_username)
    enter_text_in_element(driver, txt_box_username, 'standard_user')
    enter_text_in_element(driver, txt_box_password, 'secret_sauce')
    click_element(driver, btn_login)
    wait_until_element_is_visible(driver, "//span[contains(text(), 'adsjsakdjasd;')]")
    should_be_equal_as_strings(driver, "//span[contains(text(), 'Products')]", "asdasdasdasd")

    """
    #data = read_mysql_data("SELECT  Pname, price  from product where Pname = 'Bed'")
    #print(data)
    # driver = open_browser("https://www.saucedemo.com/")

    wait_until_element_is_visible(driver, txt_box_username)
    enter_text_in_element(driver, txt_box_username, data[3]['txt_box_username'])
    enter_text_in_element(driver, txt_box_password, data[3]['txt_box_password'])
    click_element(driver, btn_login)
    time.sleep(2)
    wait_until_element_is_visible(driver, lnk_backpack)
    click_element(driver, lnk_backpack)
    wait_until_element_is_clickbale(driver, btn_add_to_cart)
    time.sleep(2)
    click_element(driver, btn_add_to_cart)
    wait_until_element_is_visible(driver, btn_remove)
    time.sleep(10)
    recording_process.terminate()
    driver.quit()

# main method
if __name__ == "__name__":
    main()

"""
# driver = open_browser_to_link("https://artoftesting.com/samplesiteforselenium")
# driver = open_browser_incognito("https://artoftesting.com/samplesiteforselenium")
driver = open_browser("https://artoftesting.com/samplesiteforselenium" , headless=True)
wait_until_element_is_visible(driver, lnk_link_text)

# take_screenshot(driver,"first_screenshot.png")
expect_error(driver , wait_until_element_is_visible , "asdasdasdasd")
"""
"""
driver = open_browser("https://www.saucedemo.com/")
wait_until_element_is_visible(driver, '//*[@id="user-name"]')
enter_text_in_element(driver, '//*[@id="user-name"]', 'standard_user')
enter_text_in_element(driver, '//*[@id="password"]', 'secret_sauce')
click_element(driver, '//*[@id="login-button"]')
time.sleep(2)
wait_until_element_is_visible(driver, '//div[contains(text(), "Backpack")]')
click_element(driver, '//div[contains(text(), "Backpack")]')
wait_until_element_is_clickbale(driver, '//*[@id="add-to-cart-sauce-labs-backpack"]')
time.sleep(2)
click_element(driver, '//*[@id="add-to-cart-sauce-labs-backpack"]')
wait_until_element_is_visible(driver, '//*[@id="remove-sauce-labs-backpack"]')
"""
"""
driver = open_browser("https://artoftesting.com/samplesiteforselenium")
wait_until_element_is_visible(driver , lnk_link_text)
continue_on_failure(driver, should_contain , lnk_link_text , "link")
continue_on_failure(driver, should_contain , lnk_link_text , "topGrep")
#should_contain(driver , lnk_link_text , 'link')
#should_contain(driver , lnk_link_text , 'topgrep')
#should_be_equal(driver , lnk_link_text , "This is a link")
#should_be_equal(driver , lnk_link_text , "is a link")


# click_element(driver , "//button[@type='button']")

# enter_text_in_element(driver , "//input[@name = 'firstName']" , "Automation")

# scroll_element_into_view(driver, "//h2[contains(text(), 'Resources')]")

# scroll_element_into_view(driver, "//select[@id='testingDropdown']")

# select_value_in_dropdown(driver , "//select[@id='testingDropdown']" , 'Manual')

# click_element(driver , "//button[contains(text(), 'Alert Box')]")

# time.sleep(30)

# print(wait_until_element_is_visible( driver , btn_gen_alert_box))
# click_element(driver , btn_gen_alert_box)
# alert_text = handle_alert(driver)
# print(f'the alert text was {alert_text}.')
'''

result = handle_alert(driver)
print(result)
print(f'The alert text was {result}.')

'''

"""

# time.sleep(30)

"""

from library.basic_selenium_actions import *
from library.comparison_actions import *
from constants.xpath.art_of_testing import *
from library.exception_handlers import *
from constants.xpath.saucedemo import *
import time

"""
# driver = open_browser_to_link("https://artoftesting.com/samplesiteforselenium")
# driver = open_browser_to_link("https://jqueryui.com/droppable/")
