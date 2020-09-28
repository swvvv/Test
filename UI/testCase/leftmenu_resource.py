from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj.leftmenuPage import resource



class resourceTest(myunit.MyTest):
        #验证结算反馈
	def test_resource(self):
		login(self.driver).user_login()
		

		sleep(2)
		resource(self.driver).verifyls()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifyls_true.png")

		sleep(2)
		resource(self.driver).verifylsuo()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifylsuo_true.png")

		sleep(2)
		resource(self.driver).verifylshi()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifylshi_true.png")

		sleep(2)
		resource(self.driver).verifylshizy()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifylshizy_true.png")

		sleep(2)
		resource(self.driver).verifykh()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifykh_true.png")

		sleep(2)
		resource(self.driver).verifylstz()
		#po1 = caselistwy(self.driver)
		sleep(2)
		#self.assertEqual(po1.clcikwy_success_loc(),"我的未交付案件")
		function.insert_img(self.driver, "verifylstz_true.png")




if __name__ == '__main__':
	unittest.main()
