from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#from selenium.webdriver.support import expected_conditions as EC

from page_obj import base

#from selenium import webdriver
from time import sleep

class login(base.Page):#Page):
	'''用户登录页面'''
	url ='/'
	#Action
	
	saas_login_user_loc = (By.NAME, "user")
	saas_login_password_loc =(By.NAME, "password")
	saas_login_button_loc = (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div/div/a')

	def saas_login(self):
		self.find_element(*self.saas_login_user_loc).click()
		sleep(1)
		self.find_element(*self.saas_login_password_loc).click()
		#self.find_element(*self.saas_login_button_loc).click()


	login_username_loc =(By.NAME, "user")
	login_password_loc = (By.NAME, "password")
	login_button_loc = (By.XPATH, '/html/body/div[6]/div[2]/div/div/div/div/div/a')

	def login_username(self, username):
		Input1 = self.find_element(*self.login_username_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().send_keys(username).perform()
		#self.find_element(*self.login_username_loc).sendkeys(username)


	def login_password(self, password):
		Input2 = self.find_element(*self.login_password_loc)
		actions2 = ActionChains(self.driver)
		actions2.move_to_element(Input2).click().send_keys(password).perform()
		#self.find_element(*self.login_password_loc).sendkeys(password)

	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	def user_login(self, username = "admin", password="123qwe"):
		self.open()
		#self.saas_login()
		self.login_username(username)
		sleep(1)
		self.login_password(password)
		sleep(1)
		self.login_button()
		sleep(1)

	user_login_success_loc = (By.CLASS_NAME, "name")
	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).text

'''
	user_error_hint_loc = (By.XPATH, '')
	pawd_error_hint_loc =(By.XPATH, '')
	

	def user_error_hint(self):
		return self.find_element(*self.user_error_hint_loc).text

	def pawd_error_hint(self):
		return self.find_element(*self.pawd_error_hint_loc).text'''

	
