# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import codecs
import requests
import csv
# import mapApi

url = "https://hz.lianjia.com/ershoufang/%s/pg%d/"
location = "xiasha"
location = "xihu"
page = 1




def getPrice(item):
	tag = item.find(class_="info clear")
	totalPrice = tag.find(class_="priceInfo").find(class_="totalPrice").find('span').text
	unitPrice = tag.find(class_="priceInfo").find(class_="unitPrice")
	# ref = tag.find(class_="title").find('a')['href']
	# name = tag.find(class_="title").find('a')
	add = tag.find(class_="houseInfo").find('a').text
	# print(add)


	return {"tp": float(totalPrice)*10**4, 
			"up": float(unitPrice['data-price']),
			"add": add}

totalPrice = 0
totalSpace = 0
unitPrices = []
spaces = []
houses = 0
address = []
lng = []
lat = []
# content = soup.select(".content")



for page in range(1, 100):
	resp = requests.get(url % (location, page))
	soup = BeautifulSoup(resp.text, "html.parser")
	content = soup.findAll(class_="clear LOGCLICKDATA")
	if len(content) == 0:
		break
	for item in content:
		res = getPrice(item)
		tp = res['tp']
		up = res['up']
		totalPrice += tp
		totalSpace += tp/up
		unitPrices.append(up)
		spaces.append(tp/up)
		houses += 1
		# state, loc = mapApi.getLocation('杭州市' + res['add'])
		# lng.append(loc[0])
		# lat.append(loc[1])
		lng.append(0)
		lat.append(0)
		address.append(res['add'])

	fileName = 'Hangzhou/%s_%d.csv' % (location, page)

	with open(fileName, 'w', newline='', encoding='utf-8-sig') as file:
		# file.write(codecs.BOM_UTF8)
		writer = csv.writer(file)
		writer.writerows(zip(address, unitPrices, spaces, lng, lat))

	print(page)

print('Houses: %d, avarage Price: %.2f' % (houses, totalPrice/totalSpace))