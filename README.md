# SkeeterTracker
As part of the Vector Borne Disease Challenge, this prototype takes available weather data to predict vector population risk. 


Introduction: 
  
  The Triangle Global Health Consortium has partnered with MEDIC to develop an Innovation Bootcamp from January to April 2017 (http://www.triangleglobalhealth.org/innovation-bootcamp) . The vector-borne disease challenge requires an assessment of the current literature to determine if parameters (geography, climate, etc.) are available to develop a prototyped tool to track the vector of interest. Herein we have included the following:
      A shell script that pulls relevant references from PubMed and Google to a directory on your desktop computer and a summary of the relevant information and parameters. Identification of these parameters (Temperature, Humidity, Rainfall) will be used in the DeveloperTool. 
      A program in python that utilizes the console WTTR (Developed by Igor Chubin: accessed at https://github.com/chubin/wttr.in), which uses the wego repo, extracting weather information from multiple sources and delivering the information to your terminal window.
 
Requirements:
  System: Windows 2003 or later; MacOS Snow Leopard or any UNIX-based system
    Terminal is available on MacOS; download and install CygWIN for Windows Users: (https://www.cygwin.com/) Install this program using the developers instructions on the website. 
  Platypus (developed by Sveinbjorn Thordarson) is recommended for additional module development and can be accessed here: http://sveinbjorn.org/software
  PythonAnywhere is also available for free to run python scripts off of the cloud: https://www.pythonanywhere.com/pricing/ 
      The python script uses a freely available program from github: https://github.com/chubin/wttr.in which can be cloned and downloaded directly. 

Installation:
      No installation required for the scripts or single-click application.
        To Access each script
        Download the files to your downloads directory 
        Open Terminal on your MacOS. If you have a Windows computer open Cygwin and a terminal window should pop up.
Type in the following commands to run the background script:
    cd downloads
    bash 170411_SkeeterTrackerBkgd.sh
Type in the following commands to run the SkeeterTracker script:
    cd downloads
    python 170415_SkeeterTracker.py

Configuration: 
There is no configuration required for running these scripts. 

Maintainers:
(PJ Halvors) (https://github.com/PJhalvors;)
