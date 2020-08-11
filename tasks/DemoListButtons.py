def clickDemoBtn(driver):
    driver.find_element_by_xpath("//*[@href='/test']").click()
    driver.find_element_by_xpath("//*[@class='nav nav-tabs']//li[@class='tab-toggle']//*[@id='basic_example']").click()
    return driver
