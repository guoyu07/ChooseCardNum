#-*- coding: utf-8 -*-
import urllib2
import re
import time
import datetime
import os

def scrape(page):
	urlPrefix = "http://www.ha.10086.cn/mall/kh.html?c=A&sn=&o=&pn="
	urlSuffix = "&jx=&month=&day=&law=&gz_card_a=&gz_card_b=&gz_card_c=&gz_card_d=&lucky_num=&unlucky_num=&userDefined=&phoneNo=&show=&phv.phoneNo=&findway="
	url = urlPrefix + page + urlSuffix

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
			fpDest.write(cardNum + '\n')
			
		getLine = fpSource.readline()

	fpSource.close()
	fpDest.close()

def removeRepeat():
	writeNumber = 0
	fpDest1 = open('num_cmcc_1.txt', 'r')
	fpDest2 = open('num_cmcc.txt', 'a')
	
	lastNum = ''
	currentNum = fpDest1.readline()
	while currentNum:
		if (currentNum != lastNum):
			writeNumber += 1  
			fpDest2.write(currentNum)
		
		lastNum = currentNum
		currentNum = fpDest1.readline()
		
		
	fpDest1.close()
	fpDest2.close()
	
	return writeNumber
		
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
	page = 1
	if os.path.exists('num_cmcc.txt'):
		os.remove('num_cmcc.txt')
	if os.path.exists('num_cmcc_1.txt'):
		os.remove('num_cmcc_1.txt') 
			
	
	while (True):
		print('Page: '+str(page))
		scrape(str(page))
		getNum()
		number = removeRepeat()
		if (number < 1):
			print 'finished'
			break
			
		page += 1
	
	os.remove('num_cmcc_1.txt')
	os.remove('src_cmcc.txt')
	
if __name__ == '__main__':
	main()