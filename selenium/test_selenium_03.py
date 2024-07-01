# import unittest
# from selenium import webdriver
#
# class BaiduTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.browser = webdriver.Edge()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.browser.quit()
#
#     def test_page_title(self):
#         self.browser.get('https://www.baidu.com/')
#         self.assertIn('百度一下，你就知道', self.browser.title)
#
#     def test_input(self):
#         self.browser.find_element('id', 'kw').send_keys('蒲志斌')
#         # 断言 是否输入内容
#         self.assertEqual(self.browser.find_element('id', 'kw').get_attribute('value'), '蒲志斌')
#
#     def test_button(self):
#         self.browser.find_element('id', 'su').click()
#         # 断言是否点击按钮
#         self.assertEqual(self.browser.find_element('id', 'su').get_attribute('value'), '百度一下')
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaiduTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Edge()
        cls.wait = WebDriverWait(cls.browser, 10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_page_title(self):
        self.browser.get('https://www.baidu.com/')
        self.assertIn('百度一下，你就知道', self.browser.title)

    def test_input(self):
        self.browser.get('https://www.baidu.com/')
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, 'kw')))
        search_box.send_keys('蒲志斌')
        self.assertEqual(search_box.get_attribute('value'), '蒲志斌')

    def test_button(self):
        self.browser.get('https://www.baidu.com/')
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, 'kw')))
        search_box.send_keys('蒲志斌')
        search_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'su')))
        search_button.click()
        self.assertEqual(search_button.get_attribute('value'), '百度一下')

if __name__ == '__main__':
    unittest.main(verbosity=2)

