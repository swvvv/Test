from selenium.webdriver import Remote
from selenium import webdriver
from threading import Thread



def browser():
	driver = webdriver.Chrome()
	'''
	driver =None
	if browser =="chrome":
		driver = webdriver.Chrome()
	#host = '127.0.0.1:4444'
		dc = {"browserName": "Chrome"}
	#driver = Remote(command_executor = "http://" + host)#+"/wd/hub")#, desired_capbilities=dc)
	elif browser =="firefox":
		driver = webdriver.Firefox()
		dc = {"browserName": "Firefox"}
	driver.get(url)
	driver.quit()'''
	return driver

if __name__ == '__main__':	
	dr = browser()
	dr.get("http://192.168.36.126:8075")
	dr.quit()
'''
    data = {"firefox":"http://192.168.36.126:8075", "chrome":"http://192.168.36.126:8075"}

    # 构建线程 
    threads = []  
    for b, url in data.items():  
       t = Thread(target=browser,args=(b,url))
       threads.append(t)  

    # 启动所有线程
    for thr in threads:
        thr.start()'''

