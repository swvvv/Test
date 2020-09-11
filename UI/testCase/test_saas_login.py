#!/user/bin/env python
#-*-coding:utf-8-*-

#author:wanglh2
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#print('start')
		cls.browser = webdriver.Chrome()
		cls.browser.maximize_window()
		cls.browser.get("http://192.168.36.126:8075")
		cls.browser.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		#print('end')
		cls.browser.quit()
	def test_login(self):
		#print('TestCase execution')
		self.username="wanglh2@bestone.com"
		self.passwd="123qwe"
		self.elem=self.browser.find_element_by_name("user")
		self.elem.send_keys(self.username)
		self.elem2=self.browser.find_element_by_name('password')
		self.elem2.click()
		time.sleep(5)
		self.elem2.send_keys(self.passwd)

		self.submit = self.browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div/div/a')
		self.submit.click()

if __name__ == '__main__':
	unittest.main(verbosity=2)