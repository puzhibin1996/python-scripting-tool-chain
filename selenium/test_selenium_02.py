import unittest

from selenium import webdriver


#  将操作放在一起

class BaiduTestCase(unittest.TestCase):

    def setUp(self):
        self.browser=webdriver.Edge()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('https://www.baidu.com/')
        self.assertIn('百度一下，你就知道',self.browser.title)

        self.browser.find_element('id','kw').send_keys('蒲志斌')
        # 断言 是否输入内容
        self.assertEqual(self.browser.find_element('id','kw').get_attribute('value'),'蒲志斌')

        self.browser.find_element('id','su').click()
        # 断言是否点击按钮
        self.assertEqual(self.browser.find_element('id','su').get_attribute('value'),'百度一下')


if __name__ == '__main__':
    unittest.main(verbosity=2)
