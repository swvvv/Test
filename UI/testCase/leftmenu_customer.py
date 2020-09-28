from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import customer



class customerTest(myunit.MyTest):
        #验证结算反馈
	def test_customer(self):
		login(self.driver).user_login()
		

		sleep(2)
		customer(self.driver).verifykh()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifykh_true.png")

		sleep(2)
		customer(self.driver).verifykhuser()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifykhuser_true.png")

		sleep(2)
		customer(self.driver).verifykhrole()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifykhrole_true.png")

		sleep(2)
		customer(self.driver).verifykhinfo()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifykhinfo_true.png")
if __name__ == '__main__':
	unittest.main()
