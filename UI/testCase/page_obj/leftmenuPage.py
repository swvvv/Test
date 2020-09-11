from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_obj import base
from page_obj import loginPage
from time import sleep

class caselist(base.Page):#Page):
	'''左侧菜单页面'''
	url ='/'
	caselistwy_loc =(By.LINK_TEXT, "文员列表")
	caselistwymyCase_loc= (By.XPATH, "//*[@id='abcd']/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]")

	def verifywy(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistwy_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistwymyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikwy_success_loc = (By.CLASS_NAME, "tab_text")

	def clickwy_success(self):
		return self.find_element(*self.clickwy_success_loc).text

	caselistyy_loc =(By.LINK_TEXT, "运营列表")
	caselistyymyCase_loc= (By.XPATH, '//*[@id="abcd"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]')

	def verifyyy(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistyy_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistyymyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikyy_success_loc = (By.CLASS_NAME, "tab_text")
	def clickyy_success(self):
		return self.find_element(*self.clickyy_success_loc).text

	caselistxs_loc =(By.LINK_TEXT, "销售列表")
	caselistxsmyCase_loc= (By.XPATH, '//*[@id="abcd"]/div/div[1]/div[2]/div/div[1]/div[1]/div/span[2]')

	def verifyxs(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistxs_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistxsmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikxs_success_loc = (By.CLASS_NAME, "tab_text")
	def clickxs_success(self):
		return self.find_element(*self.clickxs_success_loc).text

	caselist_loc =(By.LINK_TEXT, "案件列表")
	caselistmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a')

	def verifycaselist(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselist_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcik_success_loc = (By.CLASS_NAME, "tab_text")
	def clickcaselist_success(self):
		return self.find_element(*self.click_success_loc).text

	caselistcw_loc =(By.LINK_TEXT, "财务列表")
	caselistcwmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div[2]/div[3]/a/i')

	def verifycw(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistcw_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistcwmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikcw_success_loc = (By.CLASS_NAME, "tab_text")
	def clickcw_success(self):
		return self.find_element(*self.clickcw_success_loc).text

	caselistwt_loc =(By.LINK_TEXT, "委托列表")
	caselistwtmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a')

	def verifywt(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistwt_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistwtmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikwt_success_loc = (By.CLASS_NAME, "tab_text")
	def clickwt_success(self):
		return self.find_element(*self.clickwt_success_loc).text

	caselistfw_loc =(By.LINK_TEXT, "非委列表")
	caselistfwmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a')	

	def verifyfw(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistfw_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistfwmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikfw_success_loc = (By.CLASS_NAME, "tab_text")
	def clickfw_success(self):
		return self.find_element(*self.clcikfw_success_loc).text

	caselistss_loc =(By.LINK_TEXT, "诉讼列表")
	caselistssmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a/i')	

	def verifyss(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistss_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistssmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikss_success_loc = (By.CLASS_NAME, "tab_text")
	def clickfss_success(self):
		return self.find_element(*self.clcikss_success_loc).text

	caselistds_loc =(By.LINK_TEXT, "待收案件")
	caselistdsmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/table/tbody/tr/td[1]/a/t')	

	def verifyds(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistds_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistdsmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikds_success_loc = (By.CLASS_NAME, "tab_text")
	def clickfds_success(self):
		return self.find_element(*self.clcikds_success_loc).text

	caselistal_loc =(By.LINK_TEXT, "案例查询")
	caselistalmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div[2]/a[1]/t')	

	def verifyal(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistal_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistalmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikal_success_loc = (By.CLASS_NAME, "tab_text")
	def clickal_success(self):
		return self.find_element(*self.clcikal_success_loc).text

	caselistpl_loc =(By.LINK_TEXT, "批量处理")
	caselistplmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr/td[1]/a/t')	

	def verifypl(self):
		'''self.find_element(*self.caselistwy_loc).clcik()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).clcik()'''

		Input1 = self.find_element(*self.caselistpl_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistplmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clcikpl_success_loc = (By.CLASS_NAME, "tab_text")
	def clickpl_success(self):
		return self.find_element(*self.clcikpl_success_loc).text




