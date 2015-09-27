# Variables = zc
import urllib2
import json
import os
from datetime import datetime
import widgets

os.system('clear')

zc = raw_input("Zip Code: ")

red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
warning = '\033[1;41m'
cend = '\033[1;m'


request = urllib2.Request("http://api.wunderground.com/api/" + "5e656d596653e6ac" + "/forecast10day/q/" + zc + ".json") ## 10-day forecast
response = urllib2.urlopen(request)

## Create array to hold forecast values
dateArray = []
dateArray2 = []
## Parse XML into array with only pretty date, epoch, and conditions forecast
jsonData = json.load(response)
for x in jsonData['forecast']['simpleforecast']['forecastday']:
    dateArray.append([x['date']['pretty'],x['conditions'],x['high']['fahrenheit'],x['low']['fahrenheit']])

for x in jsonData['forecast']['txt_forecast']['forecastday']:
    dateArray2.append([x['title'], x['fcttext']])


print "\nCurrent Forecast for current day, plus next 9 is:"
for x in dateArray:
    if dateArray[1] == "Overcast" or "Partly Cloudy":
        dateArray[1] = yellow + str(dateArray[1]) + cend
    else:
        dateArray[1] = dateArray[1]

    print x[0] + ", " + x[1] + ", High: " + x[2] + "F" + ", Low: " + x[3] + "F"

tf = raw_input("Text Forecast?[Y/N]: ")

if tf == "Y":
    os.system('clear')
    for x in dateArray2:
        print x[0] + ": " + x[1]
        print "--------------------------------------------------------------------"
else:
    print "Ok!"
