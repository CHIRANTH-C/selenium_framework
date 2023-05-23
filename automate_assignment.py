from library.basics_selenium_actions import *
from constants.xpath.sauce_demo import *

import time

driver = open_browser_to_link(url_link)
# time.sleep(30)

# log in details
enter_text_in_element(driver , usr_nm , "standard_user")
enter_text_in_element(driver , pwd , "secret_sauce")
click_element(driver , btn_ln)

# adds 3 products to the cart
click_element(driver , jacket_cart)
click_element(driver , bike_cart)
click_element(driver , backpack_cart)

# checkout
click_element(driver ,shopping_cart_link)
click_element(driver , btn_checkout)

# fill information
enter_text_in_element(driver ,  first_nm, "Chiranth")
enter_text_in_element(driver ,  last_nm, "C")
enter_text_in_element(driver ,  post_code, "560062")

# continue
click_element(driver , btn_continue)
click_element(driver , btn_finish)

# get text element
result_txt = get_element_text(driver , msg_text)
print(f'Result text is {result_txt}.')

time.sleep(30)