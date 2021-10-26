# Freebitco.in Automation/Bot

This script for is for those wishing to automate collecting a faucets bitcoin. 
I have other versions of this script which include captcha solving and proxies for multiple accounts. 

To sign up use this link https://freebitco.in/?r=3735019

I regularly send shares to my referals so dont be shy to join.

To begin with using this you need to be able to install Python 3.9.2

GUIDE FOR WINDOWS USERS 

Step 1
To sign up to freebitcoin

Step2 
Download and install Python 3.9.2 depending on your system.
https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe    [x64]
https://www.python.org/ftp/python/3.9.2/python-3.9.2.exe          [x32]

Step3 
Install pip packages open command console:
py -m pip install requests
py -m pip install selenium
py -m pip install pyautogui

Step 4 
Download and install cromedriver & also google chrome (You need the path of Chromedriver for the script line 117
https://chromedriver.storage.googleapis.com/96.0.4664.18/chromedriver_win32.zip

If you have installed the files necessary the script should run you will need to fill in the missing details for it to work for you. 

to run the script save the file and run it with
py path/to/script.py 

TO AUTOMATE THIS WITH WINDOWS YOU NEED TO USE TASK SCHEDULER A GUIDE CAN BE FOUND HERE https://datatofish.com/python-script-windows-scheduler/



GUIDE FOR LINUX USERS 
Step 1
To sign up to freebitcoin

Step 2
go to your terminal and use the following commands
sudo apt-get install python3
pip3 install requests
pip3 install pyautogui
pip3 install selenium
wget 'https://chromedriver.storage.googleapis.com/96.0.4664.18/chromedriver_linux64.zip'

unzip the chromedriver to /usr/bin
add the chromedriver path to the python Script line 117

Step 3
you also then need to create a bash script for the script to run in crontab to do this use this code
#!/bin/sh
'/usr/bin/python3' '/home/path/Freebitcoin.py'
exit 0.

as you can see this is the python environment path and also a path to the script, save this file somewhere you can find it for location for the next step
save this file as Freebitcoin.sh and go to the file location in the terminal

Step 4
use this command to make the bash script executable by the system:
chmod +x Freebitcoin.sh

Step 5 
Set up crontab go to the terminal and use the command:
crontab -e

for cron tables refer to 

https://study.com/academy/lesson/cron-tables-in-linux-definition-example.html

add this line to the bottom of the crontab file once you have entered the line ctrl+o to save and ctrl+x to exit the crontab file 
0 1-24 * * *   pi    export DISPLAY=:0 && '/home/path/Freebitcoin.sh'

once you have done this it should be setup to run every minute on the hour for 24 hours a day

enter terminal again and use: 
systemctl reload cron

This will reload the cron config for use.

Enjoy

Any push for a proxy/captcha version is asked for and I will release it :)








