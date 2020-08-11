from tasks.setUpDriver import Initiate
import unittest


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "https://www.seleniumeasy.com/test/"
        self.driver = Initiate.tear_up(self.url)
        self.driver.find_element_by_xpath("//*[@class='nav nav-tabs']//li[@class='tab-toggle']//*[@id='basic_example']").click()
        self.driver.find_element_by_link_text("Check Box Demo").click()

    def test_single_check_box(self):
        ele_box = self.driver.find_element_by_xpath("//*[@id='isAgeSelected']")
        box_res = ele_box.is_selected()
        self.assertFalse(box_res)
        ele_box.click()
        box_res = ele_box.is_selected()
        self.assertTrue(box_res)
        self.assertEqual("Success - Check box is checked", self.driver.find_element_by_xpath("//*[@id='txtAge']").text)

    def tearDown(self):
        self.res = Initiate.tear_down(self.driver)
        self.assertTrue(self.res)


if __name__ == '__main__':
    unittest.main()


