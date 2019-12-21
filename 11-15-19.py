#Name: Clare Lee
#Email: Clare.Lee94@myhunter.cuny.edu
#Date: November 15, 2019
#This program asks user for input and output file and creates a map with markers for all traffic collisions from input file

import folium
import pandas as pd

inFile = input("Enter CSV file name: ")
outFile = input("Enter output file: ")

readIn = pd.read_csv(inFile)

nycMap = folium.Map(
    location = [40.75,-74.125],
    zoom_start = 10,
    tiles = "OpenStreetMap"
)

for index,row in readIn.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    time = row["TIME"]
    newMarker = folium.Marker([lat,lon], popup=time)
    newMarker.add_to(nycMap)

nycMap.save(outfile=outFile)
