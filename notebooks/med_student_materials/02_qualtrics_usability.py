# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 08:23:31 2016

@author: nn31
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import scipy.stats

sus_qs = ['Ease of Use (SUS)-I think that I would like to use this application frequently.',
       'Ease of Use (SUS)-I found the application unnecessarily complex.',
       'Ease of Use (SUS)-I thought the application was easy to use.',
       'Ease of Use (SUS)-I think that I would need the support of a technical person to be able to use this application.',
       'Ease of Use (SUS)-I found the various functions in the application were well integrated.',
       'Ease of Use (SUS)-I thought there was too much inconsistency in this application.',
       'Ease of Use (SUS)-I would imagine that most people would learn to use this application very quickly.',
       'Ease of Use (SUS)-I found the application very cumbersome to use.',
       'Ease of Use (SUS)-I felt very confident using the application.',
       'Ease of Use (SUS)-I needed to learn a lot of things before I could get going with this application.']

nasa_qs = ['Cognitive Workload (NASA-TLX)-How mentally demanding was the task?',
       'Cognitive Workload (NASA-TLX)-How much time pressure did you feel?',
       'Cognitive Workload (NASA-TLX)-How successful were you in accomplishing what you were asked to do?',
       'Cognitive Workload (NASA-TLX)-How hard did you have to work to accomplish your level of performance?',
       'Cognitive Workload (NASA-TLX)-How insecure, discouraged, irritated, stressed, and annoyed were you?']

us_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Control.csv","rb"))
us_control_sus = us_control[sus_qs]
us_control_sus = us_control_sus.dropna()
us_control_nasa = us_control[nasa_qs]
us_control_nasa = us_control_nasa.dropna()
us_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Intervention.csv","rb"))
us_interve_sus = us_interve[sus_qs]
us_interve_sus = us_interve_sus.dropna()
us_interve_nasa = us_interve[nasa_qs]
us_interve_nasa = us_interve_nasa.dropna()

dd = json.load(open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback_-_Control.qsf","r"))

colors = ['b','r','c','m','y','k']
question = ['Ease of Use (SUS)-I think that I would like to use this application frequently.',
       'Ease of Use (SUS)-I found the application unnecessarily complex.',
       'Ease of Use (SUS)-I thought the application was easy to use.',
       'Ease of Use (SUS)-I think that I would need the support of a technical person to be able to use this application.',
       'Ease of Use (SUS)-I found the various functions in the application were well integrated.',
       'Ease of Use (SUS)-I thought there was too much inconsistency in this application.',
       'Ease of Use (SUS)-I would imagine that most people would learn to use this application very quickly.',
       'Ease of Use (SUS)-I found the application very cumbersome to use.',
       'Ease of Use (SUS)-I felt very confident using the application.',
       'Ease of Use (SUS)-I needed to learn a lot of things before I could get going with this application.',
       'Cognitive Workload (NASA-TLX)-How mentally demanding was the task?',
       'Cognitive Workload (NASA-TLX)-How much time pressure did you feel?',
       'Cognitive Workload (NASA-TLX)-How successful were you in accomplishing what you were asked to do?',
       'Cognitive Workload (NASA-TLX)-How hard did you have to work to accomplish your level of performance?',
       'Cognitive Workload (NASA-TLX)-How insecure, discouraged, irritated, stressed, and annoyed were you?',
       'User Satisfaction-I believe this medication display would help improve my ability to manage patients’  medications.',
       'User Satisfaction-I believe this medication display would aid me in providing a better treatment regimen for my patients.',
       'User Satisfaction-I believe this medication display would improve patient outcomes.']
       
questionsName = 'User Satisfaction-I believe this medication display would help improve my ability to manage patients’  medications.'
question_choi = ['Strongly disagree','Somewhat disagree','Neither agree nor disagree','Somewhat agree','Strongly agree']
#using this information, let's draw our bar plot
length = len(question_choi)
depths = [[0,0] for i in range(length)]
counts_control = us_control[questionsName].value_counts()
counts_interve = us_interve[questionsName].value_counts()

#replace zeros with actual data
for x in list(counts_control.index):
    if x in question_choi:
        indx = question_choi.index(x)
        depths[indx][0] = counts_control[x]
        
for x in list(counts_interve.index):
    if x in question_choi:
        indx = question_choi.index(x)
        depths[indx][1] = counts_interve[x]

#start the matplotlib stuff
n_groups = 2
fig, ax = plt.subplots()    
index = np.arange(n_groups)
bar_width = 0.15   
opacity = 0.4
error_config = {'ecolor': '0.3'}

#Use list comprehension to define the rects
rects = [plt.bar(index+(i*bar_width), x, bar_width, 
                alpha=opacity,
                color=colors[i],
                error_kw=error_config,
                label=question_choi[i]) for i,x in enumerate(depths)]      
# add some   
plt.ylabel('Total')
plt.title("\n".join(wrap(questionsName)))
plt.xticks(index + bar_width*2.5,  ('Control','Intervention'))
plt.legend()
plt.tight_layout()
plt.show()


#calculating the SUS score
def scoreResult(x):
    if x=='Strongly disagree':
        return(1)
    elif x=='Somewhat disagree':
        return(2)
    elif x=='Neither agree nor disagree':
        return(3)
    elif x=='Somewhat agree':
        return(4)
    elif x=='Strongly agree':
        return(5)
        
def even_correct(x):
    return(5-x)
def odd_correct(x):
    return(x-1)

def susIt(x):
    temp = [scoreResult(y) for y in x]
    temp_correct = [even_correct(y) if (y % 2 ==0) else odd_correct(y) for y in temp]
    result = np.sum(temp_correct)*2.5
    return(result)
       
sus_control = pd.Series(us_control_sus.apply(susIt,axis=1))
sus_interve = pd.Series(us_interve_sus.apply(susIt,axis=1))

#Calculating the NASA-TLX
def scoreResultNASA(x):
    if x=='Very low':
        return(1*4) #Note this is 1*4 - I'm equally weighting all questions by 4
    elif x=='Somewhat low':
        return(2*4) #Note this is 1*4 - I'm equally weighting all questions by 4
    elif x=='Neutral':
        return(3*4) #Note this is 1*4 - I'm equally weighting all questions by 4
    elif x=='Somewhat high':
        return(4*4) #Note this is 1*4 - I'm equally weighting all questions by 4
    elif x=='Very high':
        return(5*4) #Note this is 1*4 - I'm equally weighting all questions by 4
        
def nasaIt(x):
    temp = [scoreResultNASA(y) for y in x]
    result = np.sum(temp)
    return(result)

nasa_control =   pd.Series(us_control_nasa.apply(nasaIt,axis=1))  
nasa_interve =   pd.Series(us_interve_nasa.apply(nasaIt,axis=1))  
    
    
    
    