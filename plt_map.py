import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

blocks =["xihu", "yuhang", "xiaoshan", "xiacheng", "jianggan", "gongshu", "binjiang"]
# blocks =["xihu"]

mapUrl ='map.png'
x1, y1 = 119.989568,30.153952
x2, y2 = 120.525389,30.477685
Min, Max = 20000, 55000

fig = plt.imread(mapUrl)
Y, X = fig.shape[0], fig.shape[1]
# plt.figure(figsize=(9, 7))

# plt.scatter([100,400], [100,400], c=cm.rainbow([0.2, 1]))
locations = {}
with open('locations.scv', 'r', encoding='utf-8-sig') as file:
	reader = csv.reader(file)
	for eachRow in reader:
		# print(eachRow)
		locations[eachRow[0]] = (float(eachRow[1]), float(eachRow[2]))

xs = []
ys = []
cs = []
for block in blocks:
	fileName = 'Hangzhou/%s.csv' % block
	with open(fileName, 'r', encoding='utf-8-sig') as file:
		reader = csv.reader(file)
		for eachRow in reader:
			try:
				x, y = locations[eachRow[0]]
				# print(x,y)
				xs.append((x - x1)/(x2 - x1)*X)
				ys.append((y - y1)/(y2 - y1)*Y)
				# cs.append((float(eachRow[1]) - Min)/(Max - Min))
				cs.append(float(eachRow[1]))
			except:
				pass

cmap = plt.cm.get_cmap('rainbow')
# print(cs[:100])
colorbar = plt.scatter(xs, ys, c=cs, vmin=25000, vmax=55000, s=2.5, cmap=cmap)

print(xs[:10], ys[:10])


plt.xlim([0, X])
plt.ylim([0, Y])

left, right, button, top = 0, X, 0, Y
plt.imshow(fig, aspect='auto', extent=(left,right,button,top))
plt.colorbar(colorbar)

plt.savefig('map.pdf', format = 'pdf', bbox_inches='tight', pad_inches=0.1,  dpi=1000)
plt.show() 
