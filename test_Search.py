import time

import pytest
from selenium.webdriver.common.by import By
from confest import setup


def test_search_the_product(setup):
    driver=setup
    search=driver.find_element(By.XPATH,"//input[@name='search']").send_keys("iphone")
    driver.implicitly_wait(10)
    search_icon=driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
    time.sleep(5)
    assert driver.find_element(By.LINK_TEXT, "iPhone").is_displayed()
    time.sleep(5)
    print("For print statement use -s")
    driver.quit()


