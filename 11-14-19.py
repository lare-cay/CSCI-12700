#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 14, 2019
#This program uses folium to make a map of NYC

import folium

nycMap = folium.Map(
    location = [40.75, -74.125],
    zoom_start = 10,
    tiles = "OpenStreetMap"
)

folium.Marker(
    location = [40.768731, -73.964915],
    popup = "Hunter College"
).add_to(nycMap)

nycMap.save(outfile="nycMap.html")
