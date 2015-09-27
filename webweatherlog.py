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

    if float(temp_f) > 80:
        temp_f = str(temp_f) + " F"
    elif float(temp_f) < 54:
        temp_f = str(temp_f) + " F"
    else:
        temp_f = str(temp_f) + " F"

    if float(wind_mph) > 15:
        wind_mph = str(wind_mph) + " MPH"
    elif float(wind_mph) <= 15 and float(wind_mph) > 5:
        wind_mph = str(wind_mph) + " MPH"
    else:
        wind_mph = str(wind_mph) + " MPH"

    if float(visibility_mi) < 6:
        visibility_mi = visibility_mi + ' miles'
    else:
        visibility_mi = visibility_mi + ' miles'


    compileda = time.ctime() + "-" + str(location) + ": " + str(weather) + " | Temp: " + str(temp_f)
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
