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
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistwy_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistwymyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickwy_success_loc = (By.CLASS_NAME, "tab_text")

	def clickwy_success(self):
		return self.find_element(*self.clickwy_success_loc).text

	caselistyy_loc =(By.LINK_TEXT, "运营列表")
	caselistyymyCase_loc= (By.XPATH, '//*[@id="abcd"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]')

	def verifyyy(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistyy_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistyymyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickyy_success_loc = (By.CLASS_NAME, "tab_text")
	def clickyy_success(self):
		return self.find_element(*self.clickyy_success_loc).text

	caselistxs_loc =(By.LINK_TEXT, "销售列表")
	caselistxsmyCase_loc= (By.XPATH, '//*[@id="abcd"]/div/div[1]/div[2]/div/div[1]/div[1]/div/span[2]')

	def verifyxs(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistxs_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistxsmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickxs_success_loc = (By.CLASS_NAME, "tab_text")
	def clickxs_success(self):
		return self.find_element(*self.clickxs_success_loc).text

	caselist_loc =(By.LINK_TEXT, "案件列表")
	caselistmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a')

	def verifycaselist(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselist_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	click_success_loc = (By.CLASS_NAME, "tab_text")
	def clickcaselist_success(self):
		return self.find_element(*self.click_success_loc).text

	caselistcw_loc =(By.LINK_TEXT, "财务列表")
	caselistcwmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div[2]/div[3]/a/i')

	def verifycw(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistcw_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistcwmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickcw_success_loc = (By.CLASS_NAME, "tab_text")
	def clickcw_success(self):
		return self.find_element(*self.clickcw_success_loc).text

	caselistwt_loc =(By.LINK_TEXT, "委托列表")
	caselistwtmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a')

	def verifywt(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistwt_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistwtmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickwt_success_loc = (By.CLASS_NAME, "tab_text")
	def clickwt_success(self):
		return self.find_element(*self.clickwt_success_loc).text

	caselistfw_loc =(By.LINK_TEXT, "非委列表")
	caselistfwmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a')	

	def verifyfw(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistfw_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistfwmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickfw_success_loc = (By.CLASS_NAME, "tab_text")
	def clickfw_success(self):
		return self.find_element(*self.clickfw_success_loc).text

	caselistss_loc =(By.LINK_TEXT, "诉讼列表")
	caselistssmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]/a/i')	

	def verifyss(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistss_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistssmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickss_success_loc = (By.CLASS_NAME, "tab_text")
	def clickfss_success(self):
		return self.find_element(*self.clickss_success_loc).text

	caselistds_loc =(By.LINK_TEXT, "待收案件")
	caselistdsmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/table/tbody/tr/td[1]/a/t')	

	def verifyds(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistds_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistdsmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickds_success_loc = (By.CLASS_NAME, "tab_text")
	def clickfds_success(self):
		return self.find_element(*self.clickds_success_loc).text

	caselistal_loc =(By.LINK_TEXT, "案例查询")
	caselistalmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div[2]/a[1]/t')	

	def verifyal(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistal_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistalmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickal_success_loc = (By.CLASS_NAME, "tab_text")
	def clickal_success(self):
		return self.find_element(*self.clickal_success_loc).text

	caselistpl_loc =(By.LINK_TEXT, "批量处理")
	caselistplmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr/td[1]/a/t')	

	def verifypl(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''

		Input1 = self.find_element(*self.caselistpl_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.caselistplmyCase_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickpl_success_loc = (By.CLASS_NAME, "tab_text")
	def clickpl_success(self):
		return self.find_element(*self.clickpl_success_loc).text



class finance(base.Page):#Page):

	'''左侧菜单页面'''
	url ='/'       
	financejs_loc =(By.LINK_TEXT, "结算反馈")
	financejssearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td/div/ul/li[2]/a/div/t')


	def verifyjs(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.financejs_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.financejssearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickjs_success_loc = (By.CLASS_NAME, "tab_text")

	def clickjs_success(self):
		return self.find_element(*self.clickjs_success_loc).text

	financels_loc =(By.LINK_TEXT, "律所合同")
	financelssearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[1]/div/div/div[2]/a[2]/t')


	def verifyls(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.financels_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.financelssearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickls_success_loc = (By.CLASS_NAME, "tab_text")

	def clickls_success(self):
		return self.find_element(*self.clickls_success_loc).text

	financekp_loc =(By.LINK_TEXT, "开票")
	financekpsearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[3]/div/div[1]/div[2]/div/div/div[2]/a[2]/t')


	def verifykp(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.financekp_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.financekpsearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickkp_success_loc = (By.CLASS_NAME, "tab_text")

	def clickkp_success(self):
		return self.find_element(*self.clickkp_success_loc).text


class data(base.Page):#Page):

	'''左侧菜单页面'''
	url ='/'       
	databb_loc =(By.LINK_TEXT, "报表")
	databbsearch_loc= (By.CLASS_NAME, "button-search")


	def verifybb(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.databb_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.databbsearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickbb_success_loc = (By.CLASS_NAME, "tab_text")

	def clickbb_success(self):
		return self.find_element(*self.clickbb_success_loc).text

	datadc_loc =(By.LINK_TEXT, "导出记录")
	datadsort_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div[1]/div/div[1]/table/thead/tr/th[1]/span/i')


	def verifydc(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.datadc_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.datadsort_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickdc_success_loc = (By.CLASS_NAME, "tab_text")

	def clickdc_success(self):
		return self.find_element(*self.clickdc_success_loc).text

	datagzb_loc =(By.LINK_TEXT, "工作表")
	datagzbbx_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div/div/div[1]/div/div[4]/div/a/t')

	def verifygzb(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.datagzb_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.datagzbbx_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickgzb_success_loc = (By.CLASS_NAME, "tab_text")

	def clickgzb_success(self):
		return self.find_element(*self.clickgzb_success_loc).text

	dataybp_loc =(By.LINK_TEXT, "仪表盘")
	dataybpbx_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div/div[1]/a/t')

	def verifyybp(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.dataybp_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.dataybpbx_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickybp_success_loc = (By.CLASS_NAME, "tab_text")

	def clickybp_success(self):
		return self.find_element(*self.clickybp_success_loc).text
	
class statistics(base.Page):#Page):

	'''左侧菜单页面'''
	url ='/'       
	statisticsgl_loc =(By.LINK_TEXT, "概览分析")
	statisticsglsectab_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div[1]/div[1]/div/ul/li[2]/a/div/t')


	def verifygl(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.statisticsgl_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.statisticsglsectab_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickgl_success_loc = (By.CLASS_NAME, "tab_text")

	def clickgl_success(self):
		return self.find_element(*self.clickgl_success_loc).text

	statisticswa_loc =(By.LINK_TEXT, "委案统计")
	#statisticsglsectab_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div[1]/div[1]/div/ul/li[2]/a/div/t')


	def verifywa(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.statisticswa_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		#Input2 = self.find_element(*self.statisticsglsectab_loc)
		#actions = ActionChains(self.driver)
		#actions.move_to_element(Input2).click().perform()

	clickwa_success_loc = (By.CLASS_NAME, "tab_text")

	def clickwa_success(self):
		return self.find_element(*self.clickwa_success_loc).text

class resource(base.Page):#Page):

	'''左侧菜单页面'''
	url ='/'       
	resourcels_loc =(By.LINK_TEXT, "律师权限")
	resourcelspermission_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td/div/div[2]/span[1]')


	def verifyls(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.resourcels_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.resourcelspermission_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickls_success_loc = (By.CLASS_NAME, "tab_text")

	def clickls_success(self):
		return self.find_element(*self.clickls_success_loc).text

	resourcelsuo_loc =(By.LINK_TEXT, "律所管理")
	resourcelsuosearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[1]/div/div[1]/div[1]/div/div/div[2]/a[2]')


	def verifylsuo(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.resourcelsuo_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.resourcelsuosearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clicklsuo_success_loc = (By.CLASS_NAME, "tab_text")

	def clicklsuo_success(self):
		return self.find_element(*self.clicklsuo_success_loc).text


	resourcelshi_loc =(By.LINK_TEXT, "律师管理")
	resourcelshisearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[1]/div/div[1]/div[1]/div/div/div[3]/a[3]/i')


	def verifylshi(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.resourcelshi_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.resourcelshisearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clicklshi_success_loc = (By.CLASS_NAME, "tab_text")

	def clicklshi_success(self):
		return self.find_element(*self.clicklshi_success_loc).text

	resourcelshizy_loc =(By.LINK_TEXT, "律师资源")
	resourcelshizysearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div/div/div/div[2]/div[2]/a')


	def verifylshizy(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.resourcelshizy_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.resourcelshizysearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clicklshizy_success_loc = (By.CLASS_NAME, "tab_text")

	def clicklshizy_success(self):
		return self.find_element(*self.clicklshizy_success_loc).text


	resourcekh_loc =(By.LINK_TEXT, "客户律师")
	resourcekhsearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[1]/div/div/div[3]/a[3]')


	def verifykh(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.resourcekh_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.resourcekhsearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickkh_success_loc = (By.CLASS_NAME, "tab_text")

	def clickkh_success(self):
		return self.find_element(*self.clickkh_success_loc).text


	resourcelstz_loc =(By.LINK_TEXT, "律师拓展")
	resourcelstzsearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[1]/div/div[1]/div[2]/a/i')


	def verifylstz(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.resourcelstz_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.resourcelstzsearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clicklstz_success_loc = (By.CLASS_NAME, "tab_text")

	def clicklstz_success(self):
		return self.find_element(*self.clicklstz_success_loc).text

class operation(base.Page):#Page):

	'''左侧菜单页面'''
	url ='/'       
	operationyy_loc =(By.LINK_TEXT, "运营用户")
	operationyysearch_loc= (By.XPATH, '//*[@id="m-split2form-user_list_wrap"]/div[4]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/a[2]/t')


	def verifyyy(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.operationyy_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.operationyysearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickyy_success_loc = (By.CLASS_NAME, "tab_text")

	def clickyy_success(self):
		return self.find_element(*self.clickyy_success_loc).text

	operationyyrole_loc =(By.LINK_TEXT, "运营角色")
	operationyyrolesearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/a[2]')


	def verifyyyrole(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.operationyyrole_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.operationyyrolesearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickyyrole_success_loc = (By.CLASS_NAME, "tab_text")

	def clickyyrole_success(self):
		return self.find_element(*self.clickyyrole_success_loc).text

	operationgx_loc =(By.LINK_TEXT, "管辖范围")
	operationgx2_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[1]/div[3]/div[1]/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/div')


	def verifygx(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.operationgx_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.operationgx2_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickgx_success_loc = (By.CLASS_NAME, "tab_text")

	def clickgx_success(self):
		return self.find_element(*self.clickgx_success_loc).text

class customer(base.Page):#Page):

	'''左侧菜单页面'''
	url ='/'       
	customerkh_loc =(By.LINK_TEXT, "客户管理")
	customerkhsearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/a[2]')


	def verifykh(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.customerkh_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.customerkhsearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickkh_success_loc = (By.CLASS_NAME, "tab_text")

	def clickkh_success(self):
		return self.find_element(*self.clickkh_success_loc).text

	customerkhuser_loc =(By.LINK_TEXT, "客户用户")
	customerkhusersearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/a[2]')


	def verifykhuser(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.customerkhuser_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.customerkhusersearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickkhuser_success_loc = (By.CLASS_NAME, "tab_text")

	def clickkhuser_success(self):
		return self.find_element(*self.clickkhuser_success_loc).text

	customerkhrole_loc =(By.LINK_TEXT, "客户角色")
	customerkhrolesearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/a[2]')


	def verifykhrole(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.customerkhrole_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.customerkhrolesearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickkhrole_success_loc = (By.CLASS_NAME, "tab_text")

	def clickkhrole_success(self):
		return self.find_element(*self.clickkhrole_success_loc).text


	customerkhinfo_loc =(By.LINK_TEXT, "客户信息")
	#customerkhinfosearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/a[2]')


	def verifykhinfo(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.customerkhinfo_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		#Input2 = self.find_element(*self.customerkhsearch_loc)
		#actions = ActionChains(self.driver)
		#actions.move_to_element(Input2).click().perform()

	clickkhinfo_success_loc = (By.CLASS_NAME, "tab_text")

	def clickkhinfo_success(self):
		return self.find_element(*self.clickkhinfo_success_loc).text

class setup(base.Page):#Page):

	'''左侧菜单页面'''
	url ='/'       
	setupja_loc =(By.LINK_TEXT, "结案报告")
	#financejsmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td/div/ul/li[2]/a/div/t')


	def verifyja(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.setupja_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		#Input2 = self.find_element(*self.financejsmyCase_loc)
		#actions = ActionChains(self.driver)
		#actions.move_to_element(Input2).click().perform()

	clickja_success_loc = (By.CLASS_NAME, "tab_text")

	def clickcj_success(self):
		return self.find_element(*self.clickja_success_loc).text

	setupcj_loc =(By.LINK_TEXT, "超级登陆")
	#financejsmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td/div/ul/li[2]/a/div/t')


	def verifycj(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.setupcj_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		#Input2 = self.find_element(*self.financejsmyCase_loc)
		#actions = ActionChains(self.driver)
		#actions.move_to_element(Input2).click().perform()

	clickcj_success_loc = (By.CLASS_NAME, "tab_text")

	def clickcj_success(self):
		return self.find_element(*self.clickcj_success_loc).text

	setupjb_loc =(By.LINK_TEXT, "解绑微信")
	#financejsmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td/div/ul/li[2]/a/div/t')


	def verifyjb(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.setupjb_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		#Input2 = self.find_element(*self.financejsmyCase_loc)
		#actions = ActionChains(self.driver)
		#actions.move_to_element(Input2).click().perform()

	clickjb_success_loc = (By.CLASS_NAME, "tab_text")

	def clickjb_success(self):
		return self.find_element(*self.clickjb_success_loc).text

	setupfy_loc =(By.LINK_TEXT, "法院管理")
	setupfysearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[2]/a[2]/t')


	def verifyfy(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.setupfy_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.setupfysearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickfy_success_loc = (By.CLASS_NAME, "tab_text")

	def clickfy_success(self):
		return self.find_element(*self.clickfy_success_loc).text

	setupgn_loc =(By.LINK_TEXT, "功能模块管理")
	setupgnsearch_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div/div[3]/div[2]/a')


	def verifygn(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.setupgn_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		Input2 = self.find_element(*self.setupgnsearch_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input2).click().perform()

	clickgn_success_loc = (By.CLASS_NAME, "tab_text")

	def clickgn_success(self):
		return self.find_element(*self.clickgn_success_loc).text

	setupcps_loc =(By.LINK_TEXT, "产品树管理")
	#financejsmyCase_loc= (By.XPATH, '//*[@id="m-split2form-r"]/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td/div/ul/li[2]/a/div/t')


	def verifycps(self):
		'''self.find_element(*self.caselistwy_loc).click()
		sleep(2)
		self.find_element(*self.caselistwymyCase_loc).click()'''
		
		Input1 = self.find_element(*self.setupcps_loc)
		actions = ActionChains(self.driver)
		actions.move_to_element(Input1).click().perform()

		#Input2 = self.find_element(*self.financejsmyCase_loc)
		#actions = ActionChains(self.driver)
		#actions.move_to_element(Input2).click().perform()

	clickcps_success_loc = (By.CLASS_NAME, "tab_text")

	def clickcps_success(self):
		return self.find_element(*self.clickcps_success_loc).text
