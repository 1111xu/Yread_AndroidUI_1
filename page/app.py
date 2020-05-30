from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.MainPage import MainPage


class App:

    driver: WebDriver=None
    @classmethod
    def start(cls):
        caps = {}
        caps['platformName'] = "Android"
        caps['deviceName'] = "127.0.0.1:62001"

        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['automationName'] = 'uiautomator2'
        caps['noReset'] = False
        caps['appPackage'] = 'com.youdao.yread'
        caps['appActivity'] = '.app.presentation.infrastructure.activity.splash.SplashActivity'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        cls.driver.implicitly_wait(8)

        try:
            element = cls.driver.find_element_by_id('btnRight')
        except:
            print('PrivacyRightBtn element is not found!')
        else:
            print('同意隐私协议')
            element.click()

        try:
            element = cls.driver.find_element_by_id('iv_popup_close')
        except:
            print('PopupCloseBtn element is not found!')
        else:
            print('关闭开机弹窗')
            element.click()

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()

