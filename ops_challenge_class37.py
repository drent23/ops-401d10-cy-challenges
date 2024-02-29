#!/usr/bin/env python3

# Script Name: Web App Fingerprinting
# Author: David Renteria
# Purpose: Banner grabbing/service fingerprinting to check if target computer supports specific services (intel gathering)

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

# import modules
import requests
import webbrowser

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

# send cookie back to target site and get HTTP response
http_response = requests.get(targetsite, cookie)

# create .html file to capture HTTP response contents
html_file = "response.html"
with open(html_file, 'w') as file:
    file.write(html_file.text)

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# open w/ firefox
webbrowser.open_new_tab(html_file)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# page = requests.get(targetsite, cookies=cookie)
# page_content = page.text

# - Generate a .html file to capture the contents of the HTTP response
# with open('/home/david/Desktop/....(path)', 'w') as file:
#   file.write(page_content)

# - Open it with Firefox
# os.system("firefox /home/david/Desktop/....(path)")

# Stretch Goal
# - Give Cookie Monster hands
# 