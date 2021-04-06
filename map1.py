#  Folum covertes python code to html and css in order to build we app applications
import folium
import pandas
import json 
# add object to the map object add two markers on the lists
# create a javascript code to add a marker in the map using the leaflet libray
data = pandas.read_csv("Volcanoes.txt")
# we should convert the LAT and LON to a native python lists
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [38.58, -99.09], zoom_starts =6, titles ="Stamen Terrain" )

fgv = folium.FeatureGroup(name= "Volcanos") # greate a specific feuture group in order to added ar the layercontrol

for lt, ln, el, n in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup= str(n) + str(el) + " meters" , fill_color=color_producer(el), color = "grey", fill_opacity = 0.7 )) 

# lambda is a method to write a function for instance lambda x: x**2 ; returns x(5) tfive to the power of two which is 25 
fgp = folium.FeatureGroup(name= "Population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000  else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})) 

# add all your feuture grooups as your map
map.add_child(fgv)
map.add_child(fgp)
#layer control panel looks for objects that have been added to map.added child
map.add_child(folium.LayerControl())

map.save("Map1.html")

