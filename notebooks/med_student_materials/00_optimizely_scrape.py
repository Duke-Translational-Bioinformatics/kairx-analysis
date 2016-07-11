# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:04:03 2016

@author: benneely
"""

#Get the data from optimizely
import requests
import json
import pprint

#Get a list of all projects
url = "https://www.optimizelyapis.com/experiment/v1/projects/"
headers = {"Content-Type": "application/json","Token": "f7d5e7f4958bdaf176f84c97a93af651:baca3957"}
r = requests.get(url, headers=headers)

result = json.loads(r.text)[0]
proj_id = result['id']
#Get a list of all experiments in project
url = "https://www.optimizelyapis.com/experiment/v1/projects/" + str(proj_id) + "/experiments"
headers = {"Content-Type": "application/json","Token": "f7d5e7f4958bdaf176f84c97a93af651:baca3957"}
r = requests.get(url, headers=headers)
print(r.status_code)
result2 = json.loads(r.text)

experiment_ids = []
experiment_des = []
for x in result2:
    experiment_ids.append(x['id'])
    experiment_des.append(x['description'])
    pprint.pprint(x)
    
#Get an experiments data
url = "https://www.optimizelyapis.com/experiment/v1/experiments/" + str(experiment_ids[0]) + "/stats"
headers = {"Content-Type": "application/json","Token": "f7d5e7f4958bdaf176f84c97a93af651:baca3957"}
r = requests.get(url, headers=headers)
print(r.status_code)
result2 = json.loads(r.text)