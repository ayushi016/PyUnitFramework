from tasks.setUpDriver import Initiate
import unittest


class Test(unittest.TestCase):

    # def setUp(self) -> None:
    #     self.url = "https://www.seleniumeasy.com/test/"
    #     self.driver = Initiate.tear_up(self.url)
    #     self.driver.find_element_by_xpath("//*[@class='nav nav-tabs']//li[@class='tab-toggle']//*[@id='basic_example']").click()
    #     self.driver.find_element_by_link_text("Simple Form Demo").click()

    @classmethod
    def setUpClass(cls):
        cls.url = "https://www.seleniumeasy.com/test/"
        cls.driver = Initiate.tear_up(cls.url)
        cls.driver.find_element_by_xpath("//*[@class='nav nav-tabs']//li[@class='tab-toggle']//*[@id='basic_example']").click()
        cls.driver.find_element_by_link_text("Simple Form Demo").click()

    @classmethod
    @unittest.expectedFailure
    def tearDownClass(cls):
        # time.sleep(1)
        cls.res = Initiate.tear_down(cls.driver)
        cls.assertTrue(cls.res)

    def test_get_input(self):
        message = "Hello there"
        self.driver.find_element_by_xpath("//*[@id='get-input']//input").send_keys(message)
        self.driver.find_element_by_xpath("//*[@id='get-input']//*[@class='btn btn-default']").click()
        get_text = self.driver.find_element_by_xpath("//*[@id='user-message']//span").text
        self.assertEqual(message,get_text)

    def test_get_input_total(self):
        num1,num2 = 15,23
        self.driver.find_element_by_xpath("//*[@id='sum1']").send_keys(num1)
        self.driver.find_element_by_xpath("//*[@id='sum2']").send_keys(num2)
        self.driver.find_element_by_xpath("//*[@id='gettotal']//*[@class='btn btn-default']").click()
        get_text = self.driver.find_element_by_xpath("//*[@id='displayvalue']").text
        self.assertEqual(str(num1+num2), get_text)

    # def tearDown(self):
    #     self.res = Initiate.tear_down(self.driver)
    #     self.assertTrue(self.res)


if __name__ == '__main__':
    unittest.main()


