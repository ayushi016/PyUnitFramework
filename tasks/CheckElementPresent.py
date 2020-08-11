from selenium.common.exceptions import NoSuchElementException


def is_element_present(driver, how, what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException:
        return False

