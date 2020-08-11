from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tasks.DemoListButtons import clickDemoBtn
from tasks.setUpDriver import Initiate
from tasks.CheckElementPresent import is_element_present
import unittest


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "https://www.seleniumeasy.com/test/"
        cls.driver = Initiate.tear_up(cls.url)

    @classmethod
    @unittest.expectedFailure
    def tearDownClass(cls):
        # time.sleep(1)
        cls.res = Initiate.tear_down(cls.driver)
        cls.assertTrue(cls.res)

    # def setUp(self) -> None:
    #     self.url = "https://www.seleniumeasy.com/test/"
    #     self.driver = Initiate.tear_up(self.url)
        # self.driver = webdriver.Chrome()
        # self.driver.get(self.url)
        # self.driver.implicitly_wait(5)


    # def tearDown(self):
    #     self.res = Initiate.tear_down(self.driver)
    #     self.assertTrue(self.res)

    def test_checkTitle(self):
        self.assertIn("Selenium Easy", self.driver.title)

    def test_sideNavPresent(self):
        self.assertTrue(is_element_present(self.driver, By.XPATH, "//div[@class='panel panel-default']"))

    def test_boardPresent(self):
        self.assertTrue(is_element_present(self.driver, By.XPATH, "//div[@class='row']//div[@class='board']"))

    def test_simple_demo_btn_present(self):
        clickDemoBtn(self.driver)
        self.assertTrue(is_element_present(self.driver, By.XPATH, "//div[@class='list-group']//a[@href='./basic-first-form-demo.html']"))

    def test_all_demo_btn_present(self):
        demo_btn_list = ["Simple Form Demo", "Check Box Demo", "Radio Buttons Demo", "Select Dropdown List",
                         "Javascript Alerts", "Window Popup Modal", "Bootstrap Alerts", "Bootstrap Modals"]

        clickDemoBtn(self.driver)
        for item in demo_btn_list:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_link_text(item)).perform()
            self.assertTrue(is_element_present(self.driver, By.PARTIAL_LINK_TEXT, item))


if __name__ == '__main__':
    unittest.main()

