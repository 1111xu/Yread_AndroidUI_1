import yaml
from appium import webdriver
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import sys
print(sys.path)
import os
os.chdir("C:/Users/zhangyixian/PycharmProjects/Yread_AndroidUI_1") #注意反斜杠
for file in os.listdir(os.getcwd()):
     print(file)
sys.path.append("C:/Users/zhangyixian/PycharmProjects/Yread_AndroidUI_1")

from page.app import App


class TestDemo:

    def setup(self):
        self.search_page=App.start().to_LibraryPage()

    def test_search_po(self):

        self.search_page.search('世界')
        assert '世界' in self.search_page.get_firstbookName()

    def teardown(self):
        App.quit()



if __name__ == '__main__':
    driver = TestDemo()
    driver.setup()
    driver.test_search_po()
    driver.teardown()

