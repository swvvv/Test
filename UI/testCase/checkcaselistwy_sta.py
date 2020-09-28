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


if __name__ == '__main__':
	unittest.main()
