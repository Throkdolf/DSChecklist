from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def elementExists(xpath, driver):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True