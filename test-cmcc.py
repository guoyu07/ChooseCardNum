#-*- coding: utf-8 -*-
import urllib2
import re
import time
import datetime
import os

def scrape():
	url="http://www.ha.10086.cn/mall/kh-C.html"

	up=urllib2.urlopen(url)
	cont=up.read()
	fp = open('src_cmcc.txt', 'w')
	fp.write(cont)
	fp.close()

def getNum():
	fpSource = open('src_cmcc.txt', 'r')		#网页源代码
	fpDest = open('num_cmcc_1.txt', 'w')	#提取号码，但可能有重复
	numInLine = '<a onclick="to_pre('
	
	getLine = fpSource.readline()
	while getLine:
		if numInLine in getLine:		#找到有号码的行
			cardNum = getLine.split("'")[1]
			
		getLine = fpSource.readline()
	
def analyse():
	fp = open('src_cmcc.txt', 'r')
	cont = fp.read()
	numList = re.findall(r'1[3578]\d{9}',cont)
	fp.close()
	'''	
	regex1 = re.compile(r' ')
	regex2 = re.compile(r':')
	result1, number = re.subn(regex1, '-', time.ctime())
	result2, number = re.subn(regex2, '_', result1)
	fp = open(result2 + ".txt", 'w')
	'''
	fp1 = open('num.txt', 'w')
	for a in numList:
		fp1.write(a+'\n')
	fp1.close()
	os.remove('src.txt')

def main():
	'''
	while (True):
		time.sleep(60)
		print time.ctime()
		scrape()
		analyse()
		
		os.system('git diff num.txt')
		
		os.system('git add .')
		os.system('git commit -m "commit"')
		
		print '*'*50
		
	'''
	scrape()
	'''
	analyse()
	'''
	
if __name__ == '__main__':
	main()