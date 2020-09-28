from selenium.webdriver import Remote

#定义主机与浏览器
lists = {'http://127.0.0.1:4444/wd/hub':'chrome',
		'http://127.0.0.1:4444/wd/hub':'firefox'}

#调用remote方法
for host, browser in lists.items():
	print(host,browser)
	driver = Remote(command_executor=host, desired_capabilities={'platform':'ANY',
																'browserName':browser,
																'version':'',
																'javascriptEnabled':True})
driver.get('http://192.168.36.126:8075')

driver.quit()
