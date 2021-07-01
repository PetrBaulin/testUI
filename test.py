import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from functions import check_element_present, wait_until_present, wait_until_clickable, wait_until_visible
from login import login

browser = webdriver.Chrome()
browser.maximize_window()
actionchains = ActionChains(browser)


def test():
    browser.get("https://www.gosuslugi.ru/")
    login(browser)
    wait_until_clickable(browser, By.CSS_SELECTOR, '[data-ng-if="$root.logined"]').click()
    wait_until_clickable(browser, By.CSS_SELECTOR, '[data-ng-href="https://lk.gosuslugi.ru/settings/account"]').click()
    wait_until_clickable(browser, By.CLASS_NAME, 'edit-avatar').click()
    file_path = os.path.join(os.getcwd(), "resources", "avatar.jpeg")
    wait_until_present(browser, By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)
    element = wait_until_present(browser, By.CLASS_NAME, 'cr-slider')
    actionchains.drag_and_drop_by_offset(element, -200, 0).perform()
    wait_until_visible(browser, By.CSS_SELECTOR, '[type="button"]').click()
    assert not check_element_present(browser, By.CLASS_NAME, 'no-avatar male'), "Фото не загрузилось"

try:
    test()

finally:
    browser.quit()
