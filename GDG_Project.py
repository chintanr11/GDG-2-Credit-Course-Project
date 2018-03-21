from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import requests

url_People = 'http://api.open-notify.org/astros/'
peopleData = dict(requests.get(url_People).json())

url_ISS_Position = 'http://api.open-notify.org/iss-now/'
ISSData = dict(requests.get(url_ISS_Position).json())

s = ""
NoOfAst = peopleData['number']
listOfAst = peopleData['people']
for i in range(NoOfAst):
    item = listOfAst[i]
    s += item['name']
    s += "\n"

LatLong = ISSData['iss_position']
latitude = float(LatLong['latitude'])
longitude = float(LatLong['longitude'])
m = Basemap(projection='cyl', lon_0 = 0)
x, y = m(longitude,latitude)

m.drawmapboundary(fill_color='#3CF5F3')
m.fillcontinents(color='#C85353', lake_color='#3CF5F3')
m.plot(x, y, marker='o', color='black')
plt.title('Current ISS Location', fontsize = 12)
ax = plt.subplot(111)
ann = ax.annotate("ASTRONAUTS CURRENTLY \nAT ISS: \n"+s,
                  xy=(x, y), xycoords='data',
                  xytext=(-218, 0), textcoords='data',
                  size=10, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  transform=plt.gcf().transFigure,
                  arrowprops=dict(arrowstyle="simple", connectionstyle="arc3,rad=-0.2",fc="w"),)
plt.show()                 