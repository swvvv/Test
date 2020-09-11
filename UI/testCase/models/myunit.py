from selenium import webdriver
#from .driver import browser
import unittest
import os 

class MyTest(unittest.TestCase):
	def setUp(self):
		#self.driver = browser()
		self.driver = webdriver.Chrome()#改写后新加入
		self.driver.implicitly_wait(10)
		#self.driver.get("http://192.168.36.126:8075")
		self.driver.maximize_window()

	def tearDown(self):
		self.driver.quit()