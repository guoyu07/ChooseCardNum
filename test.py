#-*- coding: utf-8 -*-
import urllib2
import re

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
	
	fp = open("number.txt", 'w')
	for a in numList:
		fp.write(a+'\n')
	fp.close()

def main():
	scrape()
	analyse()
	
if __name__ == '__main__':
	main()