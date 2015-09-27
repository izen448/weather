import urllib2
import json
import os
from datetime import datetime
import widgets

os.system('clear')

#debugging = True
debugging = False

zc = raw_input("Zip Code: ")

f = urllib2.urlopen('http://api.wunderground.com/api/5e656d596653e6ac/geolookup/conditions/q/' + zc + '.json')
json_string = f.read()
parsed_json = json.loads(json_string)

location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
feelslike_f = parsed_json['current_observation']['feelslike_f']
wind_dir = parsed_json['current_observation']['wind_dir']
wind_mph = parsed_json['current_observation']['wind_mph']
wind_degrees = parsed_json['current_observation']['wind_degrees']
windchill_f = parsed_json['current_observation']['windchill_f']
weather = parsed_json['current_observation']['weather']
visibility_mi = parsed_json['current_observation']['visibility_mi']
relative_humidity = parsed_json['current_observation']['relative_humidity']
uv = parsed_json['current_observation']['UV']
solarradiation = parsed_json['current_observation']['solarradiation']
precip_today_in = parsed_json['current_observation']['precip_today_in']
wind_gust_mph = parsed_json['current_observation']['wind_gust_mph']
#long = ['current_observation']['display_location.latitude']
#lat = ['current_observation']['display_location.longitude']

if debugging == True:
    temp_f = raw_input("temp_f: ")
    feelslike_f = raw_input("feelslike_f: ")
    wind_dir = raw_input("wind_dir: ")
    wind_mph = raw_input("wind_mph: ")
    wind_degrees = raw_input("wind_degrees: ")
    windchill_f = raw_input("windchill_f: ")
    weather = raw_input("weather: ")
    visibility_mi = raw_input("visibility_mi: ")
    relative_humidity = raw_input("relative_humidity: ")
    uv = raw_input("uv: ")
    solarradiation = raw_input("solarradiation: ")
    precip_today_in = raw_input("precip_today_in: ")
    wind_gust_mph = raw_input("wind_gust_mph: ")
else:
    debugging = debugging


red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
yellow = '\033[1;33m'
cyan = '\033[1;36m'
warning = '\033[1;41m'
cend = '\033[1;m'

if float(temp_f) > 80:
    temp_f = red + str(temp_f) + " F" + cend
elif float(temp_f) < 54:
    temp_f = cyan + str(temp_f) + " F" + cend
else:
    temp_f = green + str(temp_f) + " F" + cend

if float(feelslike_f) > 75:
    feelslike_f = red + str(feelslike_f) + " F" + cend
elif float(feelslike_f) < 50:
    feelslike_f = cyan + str(feelslike_f) + " F" + cend
else:
    feelslike_f = green + str(feelslike_f) + " F" + cend

if float(wind_gust_mph) == 0:
    wind_gust_mph = green + str(wind_gust_mph) + cend
elif float(wind_gust_mph) >= 0.01 and float(wind_gust_mph) <= 15:
    wind_gust_mph = yellow + str(wind_gust_mph) + "MPH" + cend
elif float(wind_gust_mph) > 15 and float(wind_gust_mph) <= 30:
    wind_gust_mph = red + str(wind_gust_mph) + "MPH" + cend
else:
    wind_gust_mph = warning + str(wind_gust_mph) + "MPH" + cend

if float(wind_mph) > 15:
    wind_mph = red + str(wind_mph) + " MPH" + cend
elif float(wind_mph) <= 15 and float(wind_mph) > 5:
    wind_mph = yellow + str(wind_mph) + " MPH" + cend
else:
    wind_mph = green + str(wind_mph) + " MPH" + cend

if float(visibility_mi) < 6:
    visibility_mi = red + visibility_mi + ' miles' + cend
else:
    visibility_mi = green + visibility_mi + ' miles' + cend

if windchill_f == "NA":
    windchill_f = green + windchill_f + cend
else:
    windchill_f = windchill_f

if str(weather) == "Clear":
    weather = green + weather + cend
elif str(weather) == "Partly Cloudy":
    weather = green + weather + cend
elif str(weather) == "Thunderstorm":
    weather = warning + weather + cend
elif str(weather) == "Rain":
    weather = red + weather + cend
elif str(weather) == "Light Rain":
    weather = red + weather + cend
elif str(weather) == "Mostly Cloudy":
    weather = yellow + weather + cend
elif str(weather) == "Overcast":
    weather = yellow + weather + cend
elif str(weather) == "Fog":
    weather = yellow + weather + cend
else:
    weather = weather

if precip_today_in >= "0.01":
    precip_today_inches = cyan + str(precip_today_in) + cend
else:
    precip_today_inches = green + str(precip_today_in) + cend

if int(uv) <= 3:
    uv = green + str(uv) + cend
elif int(uv) >= 4 and int(uv) <= 6:
    uv = yellow + str(uv) + cend
else:
    uv = red + str(uv) + cend

print '\033[1;44m' + str(datetime.now().strftime("%Y-%m-%d %H:%M.%S")) + '\033[1;m'
print "Current Weather for: %s" % (location)
#print "Long: %s | Lat: %s" % (long, lat)
print "------------------------------------"
print "Current Conditions: %s" % (weather)
print "Todays Precipitation: %s inches" % (precip_today_inches)
print "------------------------------------"
print "Temp: %s  |  Feels Like: %s" % (temp_f, feelslike_f)
print "Wind Dir: %s(%s)  |  Wind Speed: %s" % (wind_dir,wind_degrees, wind_mph)
print "Wind Gust: %s  |  Wind Chill: %s" % (wind_gust_mph, windchill_f)
print "Humidity: %s  |  Visibility: %s" % (relative_humidity, visibility_mi)
print "UV Index: %s  |  Radiation : %s" % (uv, solarradiation)
print "------------------------------------"
widgets.compass(wind_dir)
print "------------------------------------"

if precip_today_in >= "0.01":
    print cyan + "          RAINFALL                  " + cend
else:
    print green + "          RAINFALL                  " + cend

widgets.rainfall(precip_today_in)
f.close
