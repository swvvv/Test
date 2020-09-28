from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import caselist

class caselistTest(myunit.MyTest):
	

	def test_caselistwy(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifywy()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifywy_true.png")
		
	def test_caselistyy(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyyy()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselistxs(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyxs()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselist(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifycaselist()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")
	
	def test_caselistcw(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifycw()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselistwt(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifywt()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselistfw(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyfw()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselistss(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyss()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselistds(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyds()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselistal(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifyal()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

	def test_caselistpl(self):
		login(self.driver).user_login()
		

		sleep(2)
		caselist(self.driver).verifypl()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")

if __name__ == '__main__':
	unittest.main()
