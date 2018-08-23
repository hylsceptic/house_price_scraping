#coding:utf-8  
import csv

fileName = "Hangzhou/xihu.csv"

with open(fileName, 'r', encoding='utf-8-sig') as file:
	reader = csv.reader(file)
	for eachRow in reader:
		print(eachRow)