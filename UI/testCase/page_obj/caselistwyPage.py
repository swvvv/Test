from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import base
import loginPage
from time import sleep

class caselistwy():#Page):
	'''用户登录页面'''
	url ='/'
	def wy(self):
		caselistwy_loc = (By.LINK_TEXT, "文员列表")
		caselistwymyCase_loc = (By.XPATH, "//*[@id='abcd']/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]")

	def clickwy(self):
		self.find_element(*self.caselistwy_loc).clcik()
		self.find_element(*self.caselistwymyCase_loc).clcik()

	def user_login(self, username = "wanglh2@bestone.com", password="123qwe"):
		self.open()
		self.saas_login()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		self.clickwy()
		sleep(1)

	clcikwy_success_loc = (By.LINK_TEXT, "我的未交付案件")
	def clickwy_success(self):
		return self.find_element(*self.clickwy_success_loc).text

