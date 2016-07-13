# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:04:03 2016

@author: benneely
"""

#Get the data from optimizely
import requests

#Get a list of all projects
url = "https://www.optimizelyapis.com/experiment/v1/projects/"
headers = {"Content-Type": "application/json","Token": ""}
r = requests.get(url, headers=headers)

result = json.loads(r.text)[0]
proj_id = result['id']
#Get a list of all experiments in project
url = "https://www.optimizelyapis.com/experiment/v1/projects/" + str(proj_id) + "/experiments"
headers = {"Content-Type": "application/json","Token": ""}
r = requests.get(url, headers=headers)
print(r.status_code)
result2 = json.loads(r.text)

experiment_ids = []
experiment_des = []
for x in result2:
    experiment_ids.append(x['id'])
    experiment_des.append(x['description'])
    pprint.pprint(x)
    
#Get an experiments data, this is a bit tricky
#it's stored in an Amazon S3 bucket