from .basics_selenium_actions import get_element_text
import logging
logging.basicConfig(
    filename='comparison.log',  # Specify the log file path
    level=logging.INFO,  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Specify the log message format
)

def should_be_equal(driver, xpath , expected_value):
    element_txt = get_element_text(driver , xpath)
    try:
        assert element_txt == expected_value
        print (f'Assertion passed , text {element_txt} not equal to expected text {expected_value}.')
    except AssertionError as e: # e is referencing the assertion error
        print(f'Assertion failed , text {element_txt} not equal to expected text {expected_value}.')
        raise AssertionError
    

def should_be_equal_as_strings(driver , xpath , expected_txt , lowercase=False):
    element_txt = get_element_text(driver , xpath)
    try:
        if lowercase:
            assert str(element_txt).lower() == str(expected_txt).lower()
        else:
            assert str(element_txt) == str(element_txt)
        print (f'Assertion passed , text {element_txt} not equal to expected text {element_txt}.')
    except AssertionError as e: # e is referencing the assertion error
        print(f'Assertion failed , text {element_txt} not equal to expected text {element_txt}.')
        raise AssertionError

def should_be_equal_as_int(driver , xpath , expected_val):
    element_val = get_element_text(driver , xpath)
    try:
        assert int(element_val) == int(expected_val)
        print (f'Assertion passed , text {element_val} not equal to expected text {expected_val}.')
    except AssertionError as e: # e is referencing the assertion error
        print(f'Assertion failed , text {element_val} not equal to expected text {expected_val}.')
        raise AssertionError

def should_be_empty(driver, xpath):
    element_text = get_element_text(driver, xpath)
    try:
        assert element_text == None or len(element_text) == 0
        print(f"Assertion passed, element text is empty.")
    except AssertionError as e: # e is referencing the assertionerror
        print(f"Assertion failed, expected empty element text, got \"{element_text}\".")
        raise AssertionError

def should_contain(driver, xpath, expected_text):
    element_text = get_element_text(driver, xpath)
    try:
        assert expected_text in element_text
        # print(f"Assertion passed, \"{element_text}\" contains \"{expected_text}\".")
        logging.info(f"Assertion passed, \"{element_text}\" contains \"{expected_text}\".")
    except AssertionError as e: # e is referencing the assertionerror
       # print(f"Assertion failed, \"{element_text}\" does not contain \"{expected_text}\".")
       # logging.error(f"Assertion failed, \"{element_text}\" does not contain \"{expected_text}\".")
        raise AssertionError(f"{e}:Assertion failed, \"{element_text}\" does not contain \"{expected_text}\".")
    

"""
def should_contain(driver, xpath, expected_text):
    element_text = get_element_text(driver, xpath)
    try:
        assert expected_text in element_text
        print(f"Assertion passed, \"{element_text}\" contains \"{expected_text}\".")
    except AssertionError as e: # e is referencing the assertionerror
        # print(f"Assertion failed, \"{element_text}\" does not contain \"{expected_text}\".")
        raise AssertionError(f"{e}: Assertion failed, \"{element_text}\" does not contain \"{expected_text}\".")
"""
         