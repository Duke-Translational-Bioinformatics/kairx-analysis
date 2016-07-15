# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:56:25 2016

@author: nn31
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import scipy.stats

cq_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/benneely/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv","rb"))
cq_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/benneely/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv","rb"))
us_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/benneely/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Control.csv","rb"))
us_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/benneely/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Usability_Survey_and_Feedback__Intervention.csv","rb"))
dd = json.load(open("/Users/benneely/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire_-_Control.qsf.txt","r"))

#In order to create the bar plots, we'll need a data structure including metadata
#Here are the questions we're interested in:
question = ['Task 1: Diabetes 1. Which medication(s) is the patient currently taking for diabetes? ',
       '2. How long has he been taking his diabetes medication(s)?',
       '3. Has he been compliant with his diabetes medication? How do you know? ',
       '4. You ask him about his diabetes medications and you can trust that he is telling you the truth...',
       '5. You see that he is currently on this maximum dose. You are wondering how recently this last ch...',
       '6. You realize that he has already taken the maximum dose of metformin for awhile without much ch...',
       '7. What was the starting dose of allopurinol prescribed for Mr. Smith? What was the last prescrib...',
       '8. Who prescribed his last refill of allopurinol? ',
       '9. You see a prescription but wonder if he has picked up his last prescription of allopurinol. Ba...',
       '10. He did not pick up his last allopurinol prescription at the pharmacy. What other agents was h...-a. No other medications have been prescribed for gout.',
       '10. He did not pick up his last allopurinol prescription at the pharmacy. What other agents was h...-b. Probenecid',
       '10. He did not pick up his last allopurinol prescription at the pharmacy. What other agents was h...-c. Naproxen',
       '10. He did not pick up his last allopurinol prescription at the pharmacy. What other agents was h...-d. Bupropion',
       '10. He did not pick up his last allopurinol prescription at the pharmacy. What other agents was h...-e. Colchicine',
       '11. After asking the patient about his gout, he explains that he has not picked up his gout medic...',
       'Task 2: Hypertension 1. Mr. Smith was diagnosed with hypertension 20 years ago. What was the firs...',
       '2. The patient’s blood pressure did not decrease in the 3 years after he was prescribed the thiaz...',
       '3. Over time, Mr. Smith’s blood pressure still continued to increase despite his compliance with...',
       '4. What do you suspect happened with his new antihypertensive regimen of HCTZ + ACE inhibitor tha...',
       '5. Despite Mr. Smith’s diligent adherence to his exercise and diet regimen and his past medicatio...',
       'Task 3: Depression  1. You continue with your check-up. The patient has a long-standing history o...-a. Selective serotonin reuptake inhibitors (SSRIs)',
       'Task 3: Depression  1. You continue with your check-up. The patient has a long-standing history o...-b. Selective norepinephrine reuptake inhibitors (SNRIs)',
       'Task 3: Depression  1. You continue with your check-up. The patient has a long-standing history o...-c. Tricyclic antidepressants (TCAs)',
       'Task 3: Depression  1. You continue with your check-up. The patient has a long-standing history o...-d. Monoamine oxidase inhibitors (MAOIs)',
       'Task 3: Depression  1. You continue with your check-up. The patient has a long-standing history o...-e. Atypical antidepressants',
       '2. Which drugs have been escalated in dose at least twice? (Check all that apply.) -a. Bupropion',
       '2. Which drugs have been escalated in dose at least twice? (Check all that apply.) -b. Sertraline',
       '2. Which drugs have been escalated in dose at least twice? (Check all that apply.) -c. Fluoxetine',
       '2. Which drugs have been escalated in dose at least twice? (Check all that apply.) -d. Duloxetine',
       '3. You ask Mr. Smith about the details of his depression medication changes in the past but he ha...',
       '4. You’d like to know what date that provider changed the medication so you can investigate the n...',
       '5. Why do you think the provider chose bupropion to prescribe in 2006? ']
#Make a histogram
import random
import numpy
from matplotlib import pyplot

x = cq_control['Q_TotalDuration']
x_min = x/60
x_min_trunc = x_min[x_min<250]
y = cq_interve['Q_TotalDuration']
y_min = y/60
y_min_trunc = y_min[y_min<250]

scipy.stats.levene(x_min_trunc,y_min_trunc)
scipy.stats.shapiro(x_min_trunc)
scipy.stats.shapiro(y_min_trunc)
scipy.stats.ttest_ind(x_min_trunc,y_min_trunc)
bins = numpy.linspace(0, 360, 36)

pyplot.hist(x_min, bins, alpha=0.5, label='Control')
pyplot.hist(y_min, bins, alpha=0.5, label='Intervention')
pyplot.legend(loc='upper left')
pyplot.show()


############
def dict_2_list(d):
    out_list = []
    for key, value in d.items():
        out_list.append(value['Display'])
    return(out_list)
colors = ['b','r','c','m','y','k']
question_inds = []
question_text = []
question_choi = []
for i,x in enumerate(dd['SurveyElements']): 
    if isinstance(x['Payload'], dict):
        if 'Choices' in list(x['Payload'].keys()):
            question_inds.append(i)
            question_text.append(x['Payload']['QuestionText'])
            question_choi.append(dict_2_list(x['Payload']['Choices']))

#Create a bar plot for multinomial questions
for i,x in enumerate(question_text):
    if 'like to know what date that' in x:
        print(i)
        print(x)
questionsName = 'Task 1: Diabetes 1. Which medication(s) is the patient currently taking for diabetes? '
dd_number = 18


#using this information, let's draw our bar plot
length = len(question_choi[dd_number])
depths = [[0,0] for i in range(length)]
#Add actual data
counts_control = cq_control[questionsName].value_counts()
counts_interve = cq_interve[questionsName].value_counts()
#replace zeros with actual data
for x in list(counts_control.index):
    if x in question_choi[dd_number]:
        indx = question_choi[dd_number].index(x)
        depths[indx][0] = counts_control[x]
        
for x in list(counts_interve.index):
    if x in question_choi[dd_number]:
        indx = question_choi[dd_number].index(x)
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
                label=question_choi[dd_number][i]) for i,x in enumerate(depths)]      
# add some   
plt.ylabel('Total')
plt.title("\n".join(wrap(questionsName)))
plt.xticks(index + bar_width*2.5,  ('Control','Intervention'))
plt.legend()
plt.tight_layout()
plt.show()

#make contengency table with p-value
cq_interve['label'] = "intervention"
cq_control['label'] = "control"
cq_interve[['label',questionsName]]
a = cq_interve[['label',questionsName]]
b= cq_control[['label',questionsName]]
cont_table = pd.concat([cq_interve[['label',questionsName]],cq_control[['label',questionsName]]],
                       axis=0)
crosstab = pd.crosstab(cont_table[questionsName], cont_table['label'], 
            rownames=[questionsName], colnames=['Arm'])
print(scipy.stats.chi2_contingency(crosstab))
print(crosstab)


crosstab = ...  
scipy.stats.chi2_contingency(
  crosstab.drop(crosstab.columns[0]).toPandas().as_matrix()
)

