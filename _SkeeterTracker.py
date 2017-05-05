#!/usr/bin/env python


# Import os for running shell functions in python
# Import smtplib for the actual sending function
# Import the email modules we'll need

import os
import smtplib
from email.mime.text import MIMEText


#Open disease surveillance websites in your internet browser
dZ = os.popen("open https://eidr-connect.eha.io/events/curated").read()
healthmap = os.popen("open http://www.healthmap.org/en/").read()

print dZ and healthmap


#Variables that define risk levels of Aedes aegypti 
greenlevel = "Low/Moderate Aedes population"
orangelevel = "Moderate Risk: remove larval habitats & avoid stagnant water"
redlevel = "High Risk: remove larval habitats & avoid stagnant water"
rainy = "Increased Aedes likely in 2-3 weeks: Remove larval habitats and stagnant water"
norain = "Increased Aedes not likely in 2-3 weeks"

#Using the shell programs curl and open
#Thanks to igor_chubin for developing WTTR
#WTTR Apache 2.0 license (https://github.com/chubin/wttr.in/blob/master/LICENSE) allows for use of this program

wttr = os.popen("curl http://wttr.in/burundi").read()

print wttr

print "Please enter current temperature as displayed above. You must enter numeric values: ",
temp = int(raw_input())

print "Please enter current humidity as displayed above. You must enter numeric values: ",
humid = int(raw_input())

print "Is there rain today or tomorrow? Please answer Yes or No",
rainfall = raw_input()



if (( temp >= 101 and humid >= 75 ) or ( temp <= 60 and humid <= 40 )) and (rainfall == "Yes"):
	TEXT = [greenlevel,rainy]
elif (( temp >= 101 and humid >= 75 ) or ( temp <= 60 and humid <= 40 )) and (rainfall == "No"):
	TEXT = [greenlevel,norain]
elif (temp >=89) and (rainfall == "No"):
	TEXT = ["Low Aedes and Anopheles risk"]
elif (temp >=89) and (rainfall == "Yes"):
	TEXT = [orangelevel,rainy]
elif (( 61 <= temp <= 70 and 40 <= humid <= 60 ) or (89 <= temp <= 100 and 40 <= humid <= 60 )) and (rainfall == "Yes"):
	TEXT = [orangelevel,rainy]
elif (( 61 <= temp <= 70 and 40 <= humid <= 60 ) or (89 <= temp <= 100 and 40 <= humid <= 60 ) or (61 <= temp <= 100)) and (rainfall == "No"):
	TEXT = [orangelevel,norain]
elif (( 71 <= temp <= 89 and 40 <= humid <= 60 )) and (rainfall == "Yes"):
	TEXT = [redlevel,rainy]
elif (( 71 <= temp <= 89 or 40 <= humid <= 60 )) and (rainfall == "No"):
	TEXT = [redlevel,norain]

SEND = os.popen(echo "str(TEXT)" | mail -s "SkeeterTracker" user@email.here).sdout.read()
print SEND