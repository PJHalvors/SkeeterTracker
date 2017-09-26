#!/usr/bin/env python

# Import os for running shell functions in python
# Import smtplib for the actual sending function
# Import the email modules we'll need
# API key is 15a4aa1feaadbd1aed88ce9bdcd15137

import os
import subprocess
import smtplib
from email.mime.text import MIMEText
import webbrowser
import urllib2
import ast
import json

#Open disease surveillance websites in your internet browser
dZ = "open https://eidr-connect.eha.io/events/curated"
healthmap = "open http://www.healthmap.org/en/"

webbrowser.open(dZ)
webbrowser.open(healthmap)



#Import Current Weather info from your city of choice

print "Where would you like to look up the current weather? Please enter your current location, substitute %20 for spaces if location is more than one word:"

# User enters their current location or one of interest

Locate = raw_input()

#Set up a variable using a string with passing variable as URL
#In short, variable = url with variable within string
#To be more specific, the Location of interest is placed within a URL from OpenWeather API that calls weather information

Weather = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=15a4aa1feaadbd1aed88ce9bdcd15137" % Locate

#Use new variable to open this website with the information
#webbrowser.open(Weather)

data = urllib2.urlopen(Weather).read(20000) #read the first 20000 alphanumeric characters in the Weather url
data = data.split("\n") #split this information into separate lines
for line in data:
	#print all of the information in your terminal window
	#print line
	if "temp" in line:
		info = ast.literal_eval(line)
		print info
	if "light rain" or "thunderstorm" in line:
		rainfall = "Yes"
		print "Chance of Rain; increased Aedes spp. population in 2-3 weeks; avoid stagnant water sources"
	else:
		print "Not currently raining"
		break
#THIS HAS TWO BUGS: FIRST IS NOT AUTOMATED EXTRACTION OF TEMP AND HUMID AND DESCRTIPTOR VALUES. THE SECOND IS USER-BASED RAW IMPUT, WHICH MAY BE ERROR=PRONE...

#Enter your temperature as a single parameter.
print "Enter Temperature. It's listed in Kelvin. We'll set it to celsius."
kelvin = float(raw_input())
temp = float(kelvin - 273)
print "Temperature is %d Celsius" % temp
print " The following temperature parameters were selected for Aedes albopictus and Aedes aegypti using the following reference: Mordecai EA, Cohen JM, Evans MV, Gudapati P, Johnson LR, Lippi CA, et al. (2017) Detecting the impact of temperature on transmission of Zika, dengue, and chikungunya using mechanistic models. PLoS Negl Trop Dis 11 (4): e0005568. https://doi.org/10.1371/journal. pntd.0005568"
print " The following temperature parameters were selected for Anopheles gambiae using the following reference: Beck-Johnson LM, Nelson WA, Paaijmans KP, Read AF, Thomas MB, Bjørnstad ON (2013) The Effect of Temperature on Anopheles Mosquito Population Dynamics and the Potential for Malaria Transmission. PLoS ONE 8(11): e79276. https://doi.org/10.1371/journal.pone.0079276

#Variables that define risk levels of Aedes aegypti and Aedes albopictus
greenlevel = "Low/Moderate Aedes population"
orangelevel = "Moderate Risk: remove larval habitats & avoid stagnant water"
redlevel = "High Risk: remove larval habitats & avoid stagnant water"

while True:
	print "Select vector of interest. Type Aedes aegypti, Aedes albopictus, or Anopheles gambiae."
	Vector = raw_input()
	if Vector == 'Aedes aegypti':
		print "Calculating Aegypti Risk. This may take a few minutes."
		if (( temp >= 35) or ( temp <= 17)):
			TEXT = [greenlevel]
		elif (( 17.1 <= temp <= 26.9) or ( 32.1<= temp <= 34.9)):
			TEXT = [orangelevel]
		elif (( 27 <= temp <= 32)):
			TEXT = [redlevel]
		print TEXT
		break
	elif Vector == 'Aedes albopictus':
		print "Calculating Albopictus Risk. This may take a few minutes."
		if (( temp >= 32) or ( temp <= 16)):
			TEXT = [greenlevel]
		elif (( 16.1 <= temp <= 22.9) or ( 29.1<= temp <= 31.9)):
			TEXT = [orangelevel]
		elif (( 23 <= temp <= 29)):
			TEXT = [redlevel]
		print TEXT
		break	
	elif Vector == 'Anopheles gambiae':
		print "Calculating Albopictus Risk. This may take a few minutes."
		if (( 40 >= temp >= 32) or ( temp <= 16)):
			TEXT = "Low Anopheles risk. "
		elif (( 16.1 <= temp <= 21.9) or ( 26.1<= temp <= 32)):
			TEXT = [orangelevel]
		elif (( 22 <= temp <= 26)):
			TEXT = [redlevel]
		elif ( temp >= 40):
			TEXT = "Lethal level for larvae, and adult Anopheles gambiae populations"
		print TEXT
		break	
	else:
		print "Invalid command. Type Aedes aegypti, Aedes albopictus, or Anopheles gambiae."

"""s=smtplib.SMTP('locaolhost')
s.sendmail(FROM, TO, "the answer is x")"""