# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 08:22:46 2016

@author: nn31
"""
import pandas as pd
import os 
cq_control = pd.read_csv(header=1,filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv"),"rb"))
cq_interve = pd.read_csv(header=1,filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv"),"rb"))
us_control = pd.read_csv(header=1,filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Control.csv"),"rb"))
us_interve = pd.read_csv(header=1,filepath_or_buffer=open(os.path.expanduser("~/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Intervention.csv"),"rb"))
contact_in = pd.read_csv(header=1,filepath_or_buffer=open(os.path.expanduser("~//Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx Contact Information.csv"),"rb"))

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