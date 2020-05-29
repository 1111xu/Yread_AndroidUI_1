import sys

sys.path.append("C:\Users\zhangyixian\PycharmProjects\Yread_AndroidUI_1")

import yaml
from appium import webdriver
import pytest
from selenium.webdriver.remote.webdriver import WebDriver


class TestDemo:
    search_data = yaml.safe_load(open('search.yaml', 'r'))
    print(search_data)

    def setup(self):
        caps = {}
        caps['platformName'] = "Android"
        caps['deviceName'] = "127.0.0.1:62001"

        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['automationName'] = 'uiautomator2'
        caps['noReset'] = False
        caps['appPackage'] = 'com.youdao.yread'
        caps['appActivity'] = '.app.presentation.infrastructure.activity.splash.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(8)

        try:
            element = self.driver.find_element_by_id('btnRight')
        except:
            print('PrivacyRightBtn element is not found!')
        else:
            print('同意隐私协议')
            element.click()

        try:
            element = self.driver.find_element_by_id('iv_popup_close')
        except:
            print('PopupCloseBtn element is not found!')
        else:
            print('关闭开机弹窗')
            element.click()

        # def loaded1(driver):
        #     print(datetime.datetime.now())
        #     if len(self.driver.find_elements_by_id('btnRight')) >= 1:
        #         self.driver.find_element_by_id('btnRight').click()
        #         return True
        #     else:
        #         return False

        # try:
        #     WebDriverWait(self.driver, 15).until(loaded('btnRight'))
        # except:
        #     print('无隐私协议弹窗')
        #
        # try:
        #     WebDriverWait(self.driver, 15).until(loaded('iv_popup_close'))
        # except:
        #     print('无开机弹窗')

    def test_getToast(self):

        self.driver.find_element_by_id('ivAvatar').click()
        print('点击头像，进入登录页')
        self.driver.find_element_by_id('btnLoginByWeChat').click()
        print('点击微信登录')
        assert '未安装微信客户端' in self.driver.find_element_by_xpath(
            "//*[@class='android.widget.Toast']").text  # 断言1：元素内容是否正确
        assert len(self.driver.find_elements_by_id('btnLoginByWeChat')) == 0  # 断言2：元素是否存在或不存在
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0));'
        #     )
        # 无需滑动操作获取页面内元素

    @pytest.mark.parametrize('PhoneNumber, Password', [  # 参数化实现多个case
        ('15888509413', 'abc12345'),
        ('13587105629', 'abc123')
    ])
    def test_loginbyPhone(self, PhoneNumber, Password):
        self.driver.find_element_by_id('ivAvatar').click()
        print('点击头像，进入登录页')
        self.driver.find_element_by_id('btnLoginByPhone').click()
        print('点击手机登录')
        self.driver.find_element_by_id('tvLoginByPassword').click()
        print('点击密码登录')
        self.driver.find_element_by_id('etPhoneNumber').send_keys(PhoneNumber)
        self.driver.find_element_by_id('etPassword').send_keys(Password)
        print('输入账号密码')
        self.driver.find_element_by_id('btnLogin').click()
        assert '徐润泽' or '测试账号' in self.driver.find_element_by_id('tvUsername').text

    @pytest.mark.parametrize('keyword', search_data)
    def test_search(self, keyword):
        self.driver.find_element_by_id('tabBookLibrary').click()
        print('点击进入图书馆')
        self.driver.find_element_by_id('tvSearch').click()
        print('点击搜索页面')
        self.driver.find_element_by_id('etSearch').send_keys(keyword)
        print('输入关键字')
        self.driver.find_element_by_id('tvSearch').click()
        print('点击搜索')

    def test_Testcase(self):
        TestCase('step.yaml').run(self.driver)

    def teardown(self):
        self.driver.quit()


class TestCase:
    def __init__(self, path):
        file = open(path, 'r')
        self.steps = yaml.safe_load(file)

    def run(self, driver: WebDriver):
        for step in self.steps:
            element = None

            if isinstance(step, dict):
                if 'id' in step.keys():
                    element = driver.find_element_by_id(step['id'])
                elif 'xpath' in step.keys():
                    element = driver.find_element_by_xpath(step['xpath'])
                else:
                    print(step.keys())

                if 'input' in step.keys():
                    element.send_keys(step['input'])
                    print(step['input'])
                else:
                    element.click()

                if 'get' in step.keys():
                    text = element.get_attribute(step['get'])
                    print(text)
