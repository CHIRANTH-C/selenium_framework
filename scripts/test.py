# from basics_functions import open_browser_to_link , click_element, enter_text_in_element,get_element_text,scroll_element_into_view,select_value_in_dropdown

# from basics_functions import *

from library.basics_selenium_actions import *
from constants.xpath.art_of_testing import *
from constants.xpath.saucedemo import *
from library.comparision_actions import *
import time

driver = open_browser("https://www.saucedemo.com/")
wait_until_element_is_visible(driver, txt_box_username)
enter_text_in_element(driver, txt_box_username, 'standard_user')
enter_text_in_element(driver, txt_box_password, 'secret_sauce')
click_element(driver, btn_login)
wait_until_element_is_visible(driver, "//span[contains(text(), 'adsjsakdjasd;')]")
should_be_equal_as_strings(driver, "//span[contains(text(), 'Products')]", "asdasdasdasd")



"""
driver = open_browser_to_link("https://www.saucedemo.com/")
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
driver = open_browser_to_link("https://artoftesting.com/samplesiteforselenium")

# click_element(driver , "//button[@type='button']")

# enter_text_in_element(driver , "//input[@name = 'firstName']" , "Automation")

# scroll_element_into_view(driver, "//h2[contains(text(), 'Resources')]")

# scroll_element_into_view(driver, "//select[@id='testingDropdown']")

# select_value_in_dropdown(driver , "//select[@id='testingDropdown']" , 'Manual')

# click_element(driver , "//button[contains(text(), 'Alert Box')]")

# time.sleep(30)

print(wait_until_element_is_visible( driver , btn_gen_alert_box))
click_element(driver , btn_gen_alert_box)
alert_text = handle_alert(driver)
print(f'the alert text was {alert_text}.')
'''

result = handle_alert(driver)
print(result)
print(f'The alert text was {result}.')

'''



time.sleep(30)

"""