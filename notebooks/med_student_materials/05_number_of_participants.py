# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 08:22:46 2016

@author: nn31
"""
import pandas as pd
import os 
import datetime

cq_control = pd.read_csv(header=1,
                         parse_dates=['StartDate','EndDate'],
                         filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv"),"rb"))
cq_interve = pd.read_csv(header=1,
                         parse_dates=['StartDate','EndDate'],
                         filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv"),"rb"))
us_control = pd.read_csv(header=1,
                         parse_dates=['StartDate','EndDate'],
                         filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Control.csv"),"rb"))
us_interve = pd.read_csv(header=1,
                         parse_dates=['StartDate','EndDate'],
                         filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Intervention.csv"),"rb"))
contact_in = pd.read_csv(header=1,
                         parse_dates=['Start Date','End Date'],
                         filepath_or_buffer=open(os.path.expanduser("~//Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx Contact Information.csv"),"rb"))

cq_control_id = set(cq_control.ResponseID)
us_control_id = set(cq_control.ResponseID)
#len(list(us_control_id.intersection(cq_control_id)))

cq_interve_id = set(cq_interve.ResponseID)
us_interve_id = set(us_interve.ResponseID)
#len(list(us_interve_id.intersection(cq_interve_id)))

contact_in_id = set(contact_in["Response ID"])
#len(list(contact_in_id.intersection(cq_control_id)))
#len(list(contact_in_id.intersection(cq_interve_id)))
#len(list(contact_in_id.intersection(us_interve_id)))








#Start limiting the contact_in data set to [June 20, July 8] as mentioned on call with Borag
grp_by_date_contact_start = contact_in['Start Date'].group_by(contact_in['Start Date'].dt.day)

#Contact info Start Date
n = len(list(contact_in['Response ID'].unique()))
contact_in_start = contact_in['Start Date']
contact_in_start = contact_in_start.dt.date
contact_in_start.groupby(contact_in_start).count().plot(kind="bar",title="Contact Info Start Date (N="+str(n)+")")

#Contact info End Date
contact_in_start = contact_in['End Date']
contact_in_start = contact_in_start.dt.date
contact_in_start.groupby(contact_in_start).count().plot(kind="bar",title="Contact Info End Date (N="+str(n)+")")



#CQ Start Date
cq = cq_control
cq = cq.append(cq_interve, ignore_index=True)
n = len(list(cq['ResponseID'].unique()))


contact_in_start = cq['StartDate']
contact_in_start = contact_in_start.dt.date
contact_in_start.groupby(contact_in_start).count().plot(kind="bar",title="CQ Info Start Date (N="+str(n)+")")

#Contact info End Date
contact_in_start = cq['EndDate']
contact_in_start = contact_in_start.dt.date
contact_in_start.groupby(contact_in_start).count().plot(kind="bar",title="CQ End Date (N="+str(n)+")")


#Usability Start Date
us = us_control
cq = us.append(us_interve, ignore_index=True)
n = len(list(cq['ResponseID'].unique()))


contact_in_start = cq['StartDate']
contact_in_start = contact_in_start.dt.date
contact_in_start.groupby(contact_in_start).count().plot(kind="bar",title="CQ Info Start Date (N="+str(n)+")")

#Contact info End Date
contact_in_start = cq['EndDate']
contact_in_start = contact_in_start.dt.date
contact_in_start.groupby(contact_in_start).count().plot(kind="bar",title="CQ End Date (N="+str(n)+")")



