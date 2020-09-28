from selenium import webdriver
import unittest
import os 
from threading import Thread

class MyTest(unittest.TestCase):
	def setUp(self):

		#self.driver = browser()
		self.driver = webdriver.Chrome()#改写后新加入
		self.driver.implicitly_wait(10)
		#self.driver.get("http://192.168.36.126:8075")
		self.driver.maximize_window()
		#self.driver.set_window_size(1920, 1080)# #(1024, 768) (4096, 3112)

	def tearDown(self):
		self.driver.quit()
