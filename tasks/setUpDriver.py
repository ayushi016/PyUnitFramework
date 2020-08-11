from selenium import webdriver
from selenium.webdriver.remote.command import Command
import time


class Initiate:

    @staticmethod
    def tear_up(url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='at-cv-lightbox-close']").click()
        return driver

    @staticmethod
    def tear_down(driver):
        time.sleep(2)
        driver.quit()
        try:
            driver.execute(Command.STATUS)
            return False
        except :
            return True


# baseURL = "https://www.google.com"
# driver = Initiate.tear_up(baseURL)
# Initiate.tear_down(driver)
