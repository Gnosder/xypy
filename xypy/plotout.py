import webbrowser
import Libs.xylib as lib
import Libs.jsonParse as parse
import gmplot
import os
import sys
from colour import Color

def tests():
    plot_out()

def plot_out():
    data, events = lib.clip_data()

    # Init Map
    lat_start = parse.latitude(data, 0)
    long_start = parse.longitude(data, 0)
    gmap = gmplot.GoogleMapPlotter(lat_start, long_start, 17)
    gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

    # Defnie Colors
    color_start = Color("red")
    color_stop = Color("white")
    gradiant_length = int(events)
    gradiant = list(color_start.range_to(color_stop, gradiant_length))

    # Choose map display
    for event in range(events):
        name_hvr = "Event number %d" % (event)
        # accuracy = parse.accuracy(data,event)
        # name_hvr = "Accuracy is %s" % (accuracy)
        # if int(accuracy) < 7:
        lat_temp = parse.latitude(data, event)
        long_temp = parse.longitude(data, event)
        gmap.marker(lat_temp, long_temp, color = str(gradiant[event]), title = name_hvr)

    # Draw map
    os.chdir(path())
    gmap.draw("output.html")

    # Open map
    html_open("output.html")


def html_open(name):
    data_path = path()
    new_cwd = os.chdir(data_path)
    data_path = data_path + name
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open_new(data_path)


def path():
    data_path = os.path.join(sys.path[0], "data/")
    return data_path


if __name__ == '__main__':
    tests()
    input("")
    try:
        tests()
    except:
        print(sys.exc_info()[0])
        input("Press Enter to exit.")
