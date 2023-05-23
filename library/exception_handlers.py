import logging
from .basics_selenium_actions import take_screenshot
# test_*.py or *_test.py
# tagging -m to run as scripts and not as module

logging.basicConfig(
    filename='automation.log',  # Specify the log file path
    level=logging.INFO,  # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Specify the log message format
)

def continue_on_failure(driver, function, *args, **kwargs):
    # args is a list of unnamed arguments - list
    # kwargs is the list of named arguments - dictionary
    try:
        function(driver, *args, **kwargs)
    except Exception as e:
        logging.error(e)
        take_screenshot(driver)

def ignore_error(driver, function, *args, **kwargs):
    try:
        function(driver, *args, **kwargs)
    except Exception as e:
        logging.info(e)
        take_screenshot(driver)

def expect_error(driver , function , *args , **kwargs):
    try:
        function(driver,*args,**kwargs)
    except Exception as e:
        logging.info ("Exception error occured: ",str(e))
        take_screenshot(driver)
    else:
        take_screenshot(driver)
        raise AssertionError("Expected error not raised")
        # take_screenshot(driver)

        