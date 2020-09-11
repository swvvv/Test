from selenium import webdriver 
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By 
import time as t

class Page(object):#obejct):
	saas_url = "http://192.168.36.126:8075"

	def __init__(self, selenium_driver,base_url=saas_url,parent=None):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30
		self.parent = parent

	def _open(self, url):
		url = self.base_url + url
		self.driver.get(url)
		assert self.on_page(),"Did not land on %s" % url

	def find_element(self, *loc):
		try:
			return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
		except NoSuchElementException as e:
			print('Error Details {0}'.format(e.args[0]))
		#return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		try:
			return WebDriverWait(self.driver,20).until(lambda
	x:x.find_elements(*loc))
		except NoSuchElementException as e:
			print('Error Details {0}'.format(e.args[0]))
		#return self.driver.find_elements(*loc)

	def open(self):
		self._open(self.url)

	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)

	def script(self, src):
		return self.driver.execute_script(src)

