from pyse import Pyse, TestCase, TestRunner

'''
used Page Object Model.
'''


class BasePage:

    def __init__(self, driver, base_url="http://www.sina.com.cn"):
        self.driver = driver
        self.base_url = base_url

    def _open(self, url):
        url = self.base_url + url
        self.driver.open(url)

    def open(self):
        self._open(self.url)


class BaiduPage(BasePage):
    url = "/"

    def search_input(self, searck_key):
        self.driver.type("id=>kw", searck_key)

    def search_button(self):
        self.driver.click("id=>su")
