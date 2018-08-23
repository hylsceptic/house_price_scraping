import requests
from ak import ak  ##api key from baidu

address = "杭州市"
def getLocation(address):
	paras = {
		"address": address,
		"output": "json",
		"ak": ak,
		# "callback": "showLocation"
	}

	url = "http://api.map.baidu.com/geocoder/v2/"

	resq = requests.get(url, params=paras)
	resq = resq.json()
	# print(resq)
	if(resq['status'] == 1):
		return (1, 0)
	else:
		location = resq['result']['location']
		return (0, (location['lng'], location['lat']))

print(getLocation(address))