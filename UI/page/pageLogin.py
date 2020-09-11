#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:linghui

from base.basePage import *
from selenium.webdriver.common.by import By

class pageLogin(WebDriver):
	username_loc = (By.ID, 'freename')
	password_loc = (By.Id, 'freepassword')
	login_loc = (By.XPATH,'')
	loginError_loc = (By.XPATH,'')

def typeUserName(self, username):
	self.findElement(*self.username_loc).send_keys(username)

def typePassword(self, password):
	self.findElement(*self.password_loc).send_keys(password)

@property
def clickLogin(self):
	self.findElement(*self.login_loc).click()

def login(self, username, password):
	self.typeUserName(username)
	self.typePassword(password)
	self.clickLogin

@property
def getLoginError(self):
	'''获取错误的信息'''
	return self.findElement(*self.loginError_loc).text

