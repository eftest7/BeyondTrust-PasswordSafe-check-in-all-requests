import config
import sys
import os
import json
import sys
import requests
import getpass
import pprint
import urllib3

#disable https warnings
urllib3.disable_warnings()

#bi server and header info
BIServer = "zhj3z7is.ps.beyondtrustcloud.com"
BaseURL="https://zhj3z7is.ps.beyondtrustcloud.com/BeyondTrust/api/public/v3"
auth_head='PS-Auth key={}; runas={};'.format(config.APIKey,config.biUsername)
header = {'Authorization': auth_head}
DataType={'Content-type':'application/json'}
session = requests.Session()
session.headers.update(header)

#Sign into BeyondInsight with URL and header information
url=BaseURL + '/Auth/SignAppin'
session.post(url=url,verify=False)

#get request id from all open requests
urlrequests = BaseURL + '/Requests'
requestslist = session.get(urlrequests,verify=False)
requestsjson = requestslist.json()
#pprint.pprint(requestsjson)

for req in requestsjson:
	#print(req['RequestID'])
    #checkin request and provide reason
        urlchkin = BaseURL + '/Requests/{}/Checkin'.format(req['RequestID'])
        print(urlchkin)
        reason= { 
                "Reason": "Demo Complete"
                }
        chkin = session.put(urlchkin, data=reason)
        
        if chkin.status_code == 204:
            print("Success! The password was used to run an Oracle command, checked the password back in, and rotated the password after running command")
        else:
            print("Error: Existing Request still open")
