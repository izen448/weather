import os

os.system('clear')

def title():
    print "----------------------"
    print "     WEATHER VEIN     "
    print "----------------------"
    print "1) Current Weather"
    print "2) Ten Day Forecast"
    print "3) Tides"
    print "4) Weather Log"
    print "5) Weather History"
    print "q) Quit"

title()

choice = raw_input(":>> ")

if choice == "1":
    import currentweather
elif choice == "2":
    import tenday
elif choice == "3":
    import tides
elif choice == "4":
    import weatherlog
elif choice == "q":
    print "BYE BYE"
else:
    print "BYE BYE!"
