# Imports
import gmplot
import webbrowser
import sys
import os
from colour import Color

# Global Variables
latitude = [37.215378, 37.223048, 37.223053, 37.223116, 37.222929]

longitude = [-93.281982, -93.272350, -93.272320, -93.272250,
             -93.272204]

# Plotter
gmap = gmplot.GoogleMapPlotter(latitude[1], longitude[1], 18)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

# gmap.scatter(latitude, longitude, '#3B0B39', size=2, marker=False)
# gmap.scatter(latitude, longitude, '#3B0B39', marker=True)
# gmap.scatter(latitude, longitude)
# gmap.plot(latitude, longitude, 'cornflowerblue', edge_width=2)
gmap.heatmap(latitude, longitude, threshold = 10, radius = 15, opacity = 1)
red = Color("red")
colors = list(red.range_to(Color("green"),5))
i = 0
for x in range(len(latitude)):
    i += 1
    print(colors[x])
    gmap.marker(latitude[x], longitude[x], color = str(colors[x]), title = i)

data_path = os.path.join(sys.path[0], "data/")
os.chdir(data_path)
gmap.draw("map_test.html")

# Open map
file_path = data_path + "map_test.html"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open_new(file_path)
