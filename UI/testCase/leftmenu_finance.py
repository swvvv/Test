from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import finance



class financeTest(myunit.MyTest):
        #验证结算反馈
	def test_financejs(self):
		login(self.driver).user_login()
		

		sleep(2)
		finance(self.driver).verifyjs()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyjs_true.png")

	def test_financels(self):
		login(self.driver).user_login()
		

		sleep(2)
		finance(self.driver).verifyls()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyls_true.png")

	def test_financekp(self):
		login(self.driver).user_login()
		

		sleep(2)
		finance(self.driver).verifykp()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifykp_true.png")

if __name__ == '__main__':
	unittest.main()
