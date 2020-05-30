import yaml
from appium import webdriver
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from page.app import App


class TestDemo:

    def setup(self):
        self.search_page=App.start().to_LibraryPage()

    def test_search_po(self):

        self.search_page.search('世界')
        assert '世界' in self.search_page.get_firstbookName()

    def teardown(self):
        App.quit()


