import os
os.system('clear')

zc = raw_input("Zip Code: ")
ct = raw_input("Check Time(seconds): ")
log = raw_input("Log File: ")

def weatherlog():
    import urllib2
    import json
    import time

    red = '\033[1;31m'
    green = '\033[1;32m'
    blue = '\033[1;34m'
    yellow = '\033[1;33m'
    cyan = '\033[1;36m'
    warning = '\033[1;41m'
    hblue = '\033[1;44m'
    cend = '\033[1;m'

    f = urllib2.urlopen('http://api.wunderground.com/api/5e656d596653e6ac/geolookup/conditions/q/' + zc + '.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)

    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    wind_dir = parsed_json['current_observation']['wind_dir']
    wind_mph = parsed_json['current_observation']['wind_mph']
    wind_degrees = parsed_json['current_observation']['wind_degrees']
    weather = parsed_json['current_observation']['weather']
    visibility_mi = parsed_json['current_observation']['visibility_mi']
    precip_today_in = parsed_json['current_observation']['precip_today_in']

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

    if float(temp_f) > 80:
        temp_f = red + str(temp_f) + " F" + cend
    elif float(temp_f) < 54:
        temp_f = cyan + str(temp_f) + " F" + cend
    else:
        temp_f = green + str(temp_f) + " F" + cend

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


    compileda = hblue + time.ctime() + cend + "-" + str(location) + ": " + str(weather) + " | Temp: " + str(temp_f)
    compiledb = "Wind Direction: " + str(wind_dir) + "(" + str(wind_degrees) + ")" + " | Wind Speed: " + str(wind_mph)
    compiledc = "Visibility: " + str(visibility_mi) + " | Today's Precipitation: " + str(precip_today_in)
    compiledd = "-----------------------------------------------------------------"
    compiledaw = "\"" + compileda + "\""
    compiledbw = "\"" + compiledb + "\""
    compiledcw = "\"" + compiledc + "\""
    compileddw = "\"" + compiledd + "\""


    print compileda
    print compiledb
    print compiledc
    print compiledd
    os.system("echo " + compiledaw + " >> " + log)
    os.system("echo " + compiledbw + " >> " + log)
    os.system("echo " + compiledcw + " >> " + log)
    os.system("echo " + compileddw + " >> " + log)


    time.sleep( int(ct) )

while True:
    weatherlog()
