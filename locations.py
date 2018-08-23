import csv
import mapApi
blocks =["xihu", "yuhang", "xiaoshan", "xiacheng", "jianggan", "gongshu", "binjiang"]

locations = set()
for block in blocks:
	fileName = 'Hangzhou/%s.csv' % block
	with open(fileName, 'r', encoding='utf-8-sig') as file:
		reader = csv.reader(file)
		for eachRow in reader:
			locations.add(eachRow[0])

lcs = []
i = 0 
for item in list(locations):
	state, loc = mapApi.getLocation('杭州市' + item)
	try:
		lng, lat = loc
	except:
		print(item, loc)
		lng, lat = 0, 0

	lcs.append([item, lng, lat])
	i += 1
	if(i%30 == 0):
		print(i)
		with open('locations.scv','w', newline='', encoding='utf-8-sig') as file:
			writer = csv.writer(file)
			writer.writerows(lcs)

print("Done.")