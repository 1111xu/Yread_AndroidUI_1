from selenium.webdriver.remote.webdriver import WebDriver


class LibraryPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword):

        self.driver.find_element_by_id('tvSearch').click()
        print('点击搜索页面')
        self.driver.find_element_by_id('etSearch').send_keys(keyword)
        print('输入关键字')
        self.driver.find_element_by_id('tvSearch').click()
        print('点击搜索')
        return self

    def get_firstbookName(self):
        return self.driver.find_element_by_id('tvBookTitle').text