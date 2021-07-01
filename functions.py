from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

def wait_until_clickable(browser, by, value, timeout=30):
    return WebDriverWait(browser, timeout).until(ec.element_to_be_clickable((by, value)))

def wait_until_visible(browser, by, value, timeout=30):
    return WebDriverWait(browser, timeout).until(ec.visibility_of_element_located((by, value)))

def wait_until_present(browser, by, value, timeout=30):
    return WebDriverWait(browser, timeout).until(ec.presence_of_element_located((by, value)))

def check_element_present(browser, by, value, timeout=5):
    try:
        if wait_until_visible(browser, by, value, timeout):
            return True
    except TimeoutException:
        return False