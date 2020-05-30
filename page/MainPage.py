from selenium.webdriver.remote.webdriver import WebDriver

from page.CoursePgae import CoursePage
from page.LibraryPage import LibraryPage


class MainPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def to_LibraryPage(self):
        self.driver.find_element_by_id('tabBookLibrary').click()
        return LibraryPage(self.driver)

    def to_CoursePage(self):
        self.driver.find_element_by_id('tabCourse').click()
        return CoursePage(self.driver)
