from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os,sys
#sys.path.append("D:/Auto/UI/testCase/page_obj")

def send_mail(file_new):
	f = open(file_new, 'rb')
	mail_body = f.read()
	f.close()

	msg = MIMEText(mail_body, 'html','utf-8')
	msg['Subject'] = Header("自动化测试报告",'utf-8')

	smtp = smtplib.SMTP()
	smtp.connect("smtp.bestone.com")
	smtp.login("wanglh2@bestone.com","aicha1989")
	smtp.sendmail("wanglh2@bestone.com","wanglh2@bestone.com",msg.as_string())
	smtp.quit()
	print("email has send out!")

def new_report(testreport):
		lists= os.listdir(testreport)
		lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" +fn))
		file_new = os.path.join(testreport,lists[-1])
		print(file_new)
		return file_new

if __name__ == '__main__':
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './UI/report/'+now+'result.html'
	fp = open(filename,"wb")
	runner = HTMLTestRunner(stream = fp, title ="SaaS系统自动化测试报告",description="环境：126，浏览器：Chrome")
	discover = unittest.defaultTestLoader.discover("./UI/testCase",pattern="*_sta.py")
	runner.run(discover)
	fp.close()
	file_path = new_report("./UI/report/")
	send_mail(file_path)