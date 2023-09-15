from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_find_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME,"btn-add-to-basket").is_displayed()
