from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import statistics



class statisticsTest(myunit.MyTest):
        #验证结算反馈
	def test_statisticsgl(self):
		login(self.driver).user_login()
		

		sleep(2)
		statistics(self.driver).verifygl()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifygl_true.png")


	def test_statisticswa(self):
		login(self.driver).user_login()
		

		sleep(2)
		statistics(self.driver).verifywa()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifywa_true.png")

if __name__ == '__main__':
	unittest.main()
