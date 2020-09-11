from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
from page_obj import base

class loginTest(myunit.MyTest):
	def user_login_verify(self,username="",password=""):
		login(self.driver).user_login(username, password)

	def test_login1(self):
		self.user_login_verify(username = "wanglh2@bestone.com",password="123qwe")
		sleep(2)
		po = login(self.driver)
		sleep(2)
		self.assertEqual(po.user_login_success(),"王玲辉")
		function.insert_img(self.driver, "user_pawd_true.png")


if __name__ == '__main__':
	unittest.main()
