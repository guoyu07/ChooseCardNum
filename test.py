#-*- coding: utf-8 -*-
import urllib2
import re
import time
import datetime
import os

def scrape():
	url="http://num.10010.com/NumApp/chseNumList/serchNums?province=76&cityCode=760&sortType=numAsc&Show4GNum=TRUE&goodsNet=4"

	up=urllib2.urlopen(url)
	cont=up.read()
	fp = open('src.txt', 'w')
	fp.write(cont)
	fp.close()

def analyse():
	fp = open('src.txt', 'r')
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

def main():
	
	while (True):
		time.sleep(60)
		print time.ctime()
		scrape()
		analyse()
		os.system('git add .')
		os.system('git diff –cached')
		os.system('git commit -m "commit"')
		print '*'*50
		
	'''
	scrape()
	analyse()
	'''
	
if __name__ == '__main__':
	main()