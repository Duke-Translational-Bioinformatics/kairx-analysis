# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:56:25 2016

@author: nn31
"""

import pandas as pd

cq_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv","rb"))
cq_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv","rb"))
us_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Control.csv","rb"))
us_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Intervention.csv","rb"))

