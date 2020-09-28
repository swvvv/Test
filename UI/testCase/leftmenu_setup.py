from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import setup



class setupTest(myunit.MyTest):
        #验证结算反馈
	def test_setup(self):
		login(self.driver).user_login()
		

		sleep(2)
		setup(self.driver).verifyja()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyja_true.png")

		#sleep(2)
		#setup(self.driver).verifycj()
		#po1 = caselistwy(self.driver)
		#sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		#function.insert_img(self.driver, "verifycj_true.png")

		sleep(2)
		setup(self.driver).verifyjb()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyjb_true.png")

		sleep(2)
		setup(self.driver).verifyfy()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyfy_true.png")


		sleep(2)
		setup(self.driver).verifygn()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifygn_true.png")


		sleep(2)
		setup(self.driver).verifycps()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifycps_true.png")




if __name__ == '__main__':
	unittest.main()
