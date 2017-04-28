#/!/bin/bash

Brave="/Applications/Brave.app"
Safari="/Applications/Safari.app"
Chrome="/Applications/Chrome.app"

echo """

Here's some background info for SkeeterTracker: an SMS based system to track Aedes Aegypti
Triangle Global Health Innovation Bootcamp
Vector Borne Disease Challenge

T Ball
T Hinton
P Tran
S Lola
P Halvorsen



"""

if ( test -e "Safari"); then echo "Safari browser exists"
else echo "Safari DNE"; fi
open "http://www.triangleglobalhealth.org/innovation-bootcamp" "$Brave"

echo """

#[1]Choose 1 key disease vector of concern (mosquito, tick, bat, mouse, bird, etc.)
#[2]Assess whether the evidence base is sufficient to predict its range and distribution with existing weather/climate data sets.
#[3]Select a relevant geographic scale and time scale.
#[4]Work with data custodians and end users to develop an app that can deploy simple risk information (e.g., “watch” and “warning”) for that geographic and time scale.
#[5]Test and deploy the system.

"""

echo """

Climate Datasets available on:

Proprietary:
https://openweathermap.org/price
http://www.hearne.software/Software/CLIMEX-DYMEX/Editions
http://www.wolframalpha.com/input/?i=climate+latitude+40.5,+longitude+-98.5

open source (US):
https://weather.com/
http://w1.weather.gov/xml/current_obs/
http://w1.weather.gov/xml/current_obs/seek.php
http://www.worldclim.org/

opensource(burundi)
http://www.wolframalpha.com/input/?i=weather+in+burundi
https://www.wunderground.com/cgi-bin/findweather/getForecast?query=burundi
http://wttr.in/burundi


"""

echo """

Iterative literature searches:
#open https://www.ncbi.nlm.nih.gov/pubmed/?term=aedes+climate $Brave
#open https://www.ncbi.nlm.nih.gov/pubmed/?term=aedes+aegypti+climate $Brave
#open https://www.ncbi.nlm.nih.gov/pubmed/?term=%22aedes+aegypti%22+climate+and+(Temperature+OR+humidity+OR+precipitation) $Brave

"""
echo "Setting up directory"


cd ~/Desktop
mkdir ~/Desktop/TGHC_2017_VBDC

echo """

Retrieving relevant publications from PubMed
"""
open "https://www.ncbi.nlm.nih.gov/pubmed/24893017" "$Brave"
open "http://datadryad.org/resource/doi:10.5061/dryad.47v3c" "$Brave"
open "http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0162649&type=printable" "$Brave"
open "http://currents.plos.org/outbreaks/article/on-the-seasonal-occurrence-and-abundance-of-the-zika-virus-vector-mosquito-aedes-aegypti-in-the-contiguous-united-states/" "$Brave"
open "https://parasitesandvectors.biomedcentral.com/articles/10.1186/s13071-017-2025-8" "$Brave"

curl -o ~/Desktop/TGHC_2017_VBDC/USAID_Burundi.pdf "http://pdf.usaid.gov/pdf_docs/PA00J1XT.pdf"
curl -o ~/Desktop/TGHC_2017_VBDC/Vector1.pdf "https://ehp.niehs.nih.gov/wp-content/uploads/125/4/EHP218.alt.pdf"
curl -o ~/Desktop/TGHC_2017_VBDC/Vector2.pdf "http://geospatialhealth.net/index.php/gh/article/view/29/29.pdf"
curl -o ~/Desktop/TGHC_2017_VBDC/PMC4909611.pdf "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4909611/pdf/main.pdf"
curl -o ~/Desktop/TGHC_2017_VBDC/Vector3.pdf "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4493829/pdf/sdata201535.pdf"
curl -o ~/Desktop/TGHC_2017_VBDC/Vector4.pdf "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2885398/pdf/1475-2875-9-114.pdf"
curl -o ~/Desktop/TGHC_2017_VBDC/Vector5.pdf "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3243685/pdf/pntd.0001378.pdf"
curl -o ~/Desktop/TGHC_2017_VBDC/Vector6.pdf "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3510154/pdf/pntd.0001908.pdf"

echo """

Findings:

#[1] Several papers match climate factors with disease incidence/prevalence
#[2] Temperature is a better disease vector indicator than rainfall
#[3] Rainfall is a predictor for increase approximately 2-3 weeks after event

Target vector: Aedes Aegypti
Target location: Burundi
Parameters: Temperature and Humidity
"""
