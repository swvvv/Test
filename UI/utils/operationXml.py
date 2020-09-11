#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:linghui

import os
import xml.dom.minidom

class OperationXml(object):
	def dir_base(self, fileName, filePath = 'data'):
		'''
		获取data文件夹下的文件
		：param fileName:要读的文件名称
		：param filePath:要读的文件名对应的文件夹
		'''
		return os.path.join(os.path.dirname(os.path.dirname(__file__)),filePath, fileName)