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

	def test_caselist(self):
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

	#test_caselistwy
		self.browser.find_element_by_link_text("文员列表").click()
		time.sleep(5)
		self.browser.find_element_by_xpath('//*[@id="abcd"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]').click()
		time.sleep(5)

	#test_caselistyy
		self.browser.find_element_by_link_text("运营列表").click()
		time.sleep(5)
		self.browser.find_element_by_xpath('//*[@id="abcd"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]').click()
		time.sleep(5)
	#test_caselistxs
		self.browser.find_element_by_link_text("销售列表").click()
		time.sleep(5)
		self.browser.find_element_by_xpath('//*[@id="abcd"]/div/div[1]/div[2]/div/div[1]/div[1]/div/span[2]').click()
		time.sleep(5)
	#test_caselist
		self.browser.find_element_by_link_text("案件列表").click()
		time.sleep(5)
		self.browser.find_element_by_link_text('搜索').click()
		time.sleep(5)
	#test_caselistfinancial
		self.browser.find_element_by_link_text("财务列表").click()
		time.sleep(5)
		self.browser.find_element_by_xpath('//*[@id="m-split2form-r"]/div/div/div/div/div/div[2]/div[3]/a/i').click()
		time.sleep(5)
	#test_caselistfw
		self.browser.find_element_by_link_text("非委列表").click()
		time.sleep(5)
		self.browser.find_element_by_xpath('//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a').click()
		time.sleep(5)
		#test_casesearch
		self.browser.find_element_by_link_text("案例查询").click()
		time.sleep(5)
		self.browser.find_element_by_xpath('//*[@id="m-split2form-r"]/div/div/div/div/div/div[2]/a[1]/t').click()
		time.sleep(5)
if __name__ == '__main__':
	#suite = unittest.TestSuite()
	#suite.addTest(LoginTest('test_login'))
	#suite.addTest(LoginTest('test_caselistwy'))
	#unittest.main(verbosity=2).run(suite)
	unittest.main(verbosity=2)