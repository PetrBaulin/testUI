from selenium.webdriver.common.by import By

from functions import wait_until_clickable

def login(browser):
    wait_until_clickable(browser, By.ID, 'auth').click()
    wait_until_clickable(browser, By.CSS_SELECTOR, '[data-bind="value: login.val"]').send_keys("login")
    wait_until_clickable(browser, By.CSS_SELECTOR, '[data-bind="value: pwd.val"]').send_keys("pw")
    wait_until_clickable(browser, By.CSS_SELECTOR, '[data-bind="click: loginByPwd"]').click()