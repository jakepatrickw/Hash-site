from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# class FunctionalTestCase(TestCase):

#     def setUp(self):
#         binary = FirefoxBinary()
#         self.browser = webdriver.Firefox(firefox_binary=binary)

#     def test_home_page(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter hash', self.browser.page_source)

#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000')
#         text = self.browser.find_element_by_id('id_text')
#         text.send_keys('hello')
#         self.browser.find_element_by_name('submit').click()
#         self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', \
#                        self.browser.page_source)

#     def tearDown(self):
#         self.browser.quit()


# class FunctionalTestCase_01(TestCase):
    
#     def setUp(self):
#         binary = FirefoxBinary()
#         self.browser = webdriver.Firefox(firefox_binary=binary)

#     def test_thing(self):        
#         self.browser.get('http://localhost:8000')
#         self.assertIn('install', self.browser.page_source)
        
#     def tearDown(self):
#         self.browser.quit()

class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.hmtl')
        
