from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import caselist


class caselistTest(myunit.MyTest):
	
        #验证文员列表
	def test_caselistwy(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifywy()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifywy_true.png")
		
        #验证运营列表		
	def test_caselistyy(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyyy()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	#验证销售列表	
	def test_caselistxs(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyxs()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyxs_true.png")

        #验证案件列表	
	def test_caselist(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifycaselist()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifycaselist_true.png")
		
        #验证财务列表
	def test_caselistcw(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifycw()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifycw_true.png")

        #验证委托列表
	def test_caselistwt(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifywt()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifywt_true.png")

        #验证非委列表
	def test_caselistfw(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyfw()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyfw_true.png")

        #验证诉讼列表
	def test_caselistss(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyss()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyss_true.png")

        #验证待收案件
	def test_caselistds(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyds()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyds_true.png")

        #验证案例查询
	def test_caselistal(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyal()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyal_true.png")

        #验证批量处理
	def test_caselistpl(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifypl()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifypl_true.png")

if __name__ == '__main__':
	unittest.main()
