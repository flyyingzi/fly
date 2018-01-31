from pyselenium import Pyse, TestCase, TestRunner
from page import BaiduPage

class BaiduTest(TestCase):
    ''' Baidu serach test case'''

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")

    def test_case(self):
        ''' baidu search key : pyse '''
        bd = BaiduPage(self.driver)
        bd.open()
        # bd.search_input("pyse")
        # bd.search_button()
        # self.assertTitle("pyse_百度搜索")


if __name__ == '__main__':
    runner = TestRunner('./', '百度测试用例', '测试环境：Firefox')
    runner.debug()
