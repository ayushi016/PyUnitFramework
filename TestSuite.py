from HTMLTestRunner import HTMLTestRunner
from tests import test_HomePage
from tests import test_simpleFormDemoPage
import unittest
import os

home = unittest.TestLoader().loadTestsFromTestCase(test_HomePage.Test)
# demo = unittest.TestLoader().loadTestsFromTestCase(test_simpleFormDemoPage.Test)
test_suite = unittest.TestSuite([home])
# test_suite.addTest(home)
# test_suite.addTest(test_HomePage('test_all_demo_btn_present'))


# generate test report on terminal
# unittest.TextTestRunner(verbosity=2).run(test_suite)

# generate HTML report
dir = os.getcwd()

# open the report file
file = open(dir + "/Test Reports/Test Summary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)





# loader = TestLoader()
# start_dir = '/Users/username/PycharmProjects/project'
# suite = loader.discover(start_dir, pattern='pm_*.py')
# runner = TextTestRunner()
# runner.run(suite)


