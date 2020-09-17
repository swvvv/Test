from selenium.webdriver import Remote
from selenium import webdriver

def browser():
	driver = webdriver.Firefox()
	#host = '127.0.0.1:4444'
	dc = {"browserName": "chrome"}
	#driver = Remote(command_executor = "http://" + host)#+"/wd/hub")#, desired_capbilities=dc)

	return driver

if __name__ == '__main__':	
	dr = browser()
	dr.get("http://192.168.36.126:8075")
	dr.quit()
