from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import data



class dataTest(myunit.MyTest):
        #验证结算反馈
	def test_databb(self):
		login(self.driver).user_login()
		

		sleep(2)
		data(self.driver).verifybb()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifybb_true.png")

	def test_datadc(self):
		login(self.driver).user_login()
		

		sleep(2)
		data(self.driver).verifydc()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifydc_true.png")

	def test_datagzb(self):
		login(self.driver).user_login()
		

		sleep(2)
		data(self.driver).verifygzb()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifygzb_true.png")

	def test_dataybp(self):
		login(self.driver).user_login()
		

		sleep(2)
		data(self.driver).verifyybp()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyybp_true.png")

if __name__ == '__main__':
	unittest.main()
