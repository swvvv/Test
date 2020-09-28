from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import operation



class operationTest(myunit.MyTest):
        #验证结算反馈
	def test_operation(self):
		login(self.driver).user_login()

		sleep(2)
		operation(self.driver).verifyyyrole()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyyrole_true.png")

		sleep(2)
		operation(self.driver).verifygx()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifygx_true.png")
		

		sleep(2)
		operation(self.driver).verifyyy()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyyy_true.png")



if __name__ == '__main__':
	unittest.main()
