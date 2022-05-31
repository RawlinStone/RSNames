import requests
import time
import json
import urllib.request
import http.client, sys
from urllib.request import Request, urlopen

site = "https://apps.runescape.com/runemetrics/profile/profile?user="
namefile = open("CheckNames.txt", 'r')
writefile = open("CheckedNames.txt", "w")

def check(username):
    z = username.replace(" ", "_")

    req = Request(site+z, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode()
    detector = True
    if webpage.find("error")!=-1:
      detector = False #if we found one
    #otherwise it's still true
    if detector == False:
        if webpage.find("NOT_A_MEMBER") != -1:
            pass
            #print(f"{username} is currently banned.")
        elif webpage.find("NO_PROFILE") != -1:
            pass
            #writefile.write(f"{username} could be available.")
            #print(f"{username} could be available.")
        elif webpage.find("PROFILE_PRIVATE") != -1:
            pass
            #print(f"{username} is private, not banned.")
        elif webpage.find("NO_PROFILE") != -1 and webpage.find("loggedIn") == -1:
            writefile.write(f"{username} is likely available.")
            #print(f"{username} is likely available.")
        else:
            writefile.write(f"{username} is likely available.")
            #print(f"{username} is likely available.")
            
    else:
        pass
        #print(username + " is taken.")




for name in namefile:
    #print(name)
    check(name)

namefile.close()
writefile.close()
print("done checking names")
