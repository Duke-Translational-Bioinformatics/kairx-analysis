# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:13:17 2016

@author: nn31
"""

import pandas as pd
import json


cq_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv","rb"))
cq_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv","rb"))

#may need this file to help answer the questions below
meta = json.load(open('/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire_-_Control.qsf','r'))
new = dict()
for i,x in enumerate(meta.get('SurveyElements')):
    payload = x.get('Payload')
    if isinstance(payload,dict):
        if any("GradingData" in s for s in list(payload.keys())):
            answers = payload.get('GradingData')
            text = []
            for z in answers:
                answer = z.get('ChoiceID')
                text.append(payload.get('Choices').get(answer).get('Display'))
            new[payload.get('QuestionDescription')] = text

#perception
tier1 = ['4. You ask him about his diabetes medications and you can trust that he is telling you the truth...',
         '6. You realize that he has already taken the maximum dose of metformin for awhile without much ch...',
         '7. What was the starting dose of allopurinol prescribed for Mr. Smith? What was the last prescrib...',
         '8. Who prescribed his last refill of allopurinol? ',
         '3. You ask Mr. Smith about the details of his depression medication changes in the past but he ha...',
         'Task 1: Diabetes 1. Which medication(s) is the patient currently taking for diabetes? '
         ]
#comprehension         
tier2 = ['2. How long has he been taking his diabetes medication(s)?',
         '3. Has he been compliant with his diabetes medication? How do you know? ',
         '5. You see that he is currently on this maximum dose. You are wondering how recently this last ch...',
         '9. You see a prescription but wonder if he has picked up his last prescription of allopurinol. Ba...',
         '10. He did not pick up his last allopurinol prescription at the pharmacy. What other agents was h...-c. Naproxen',
         '10. He did not pick up his last allopurinol prescription at the pharmacy. What other agents was h...-e. Colchicine',
         'Task 2: Hypertension 1. Mr. Smith was diagnosed with hypertension 20 years ago. What was the firs...',
         '3. Over time, Mr. Smith’s blood pressure still continued to increase despite his compliance with...',
         'Task 3: Depression  1. You continue with your check-up. The patient has a long-standing history o...-a. Selective serotonin reuptake inhibitors (SSRIs)',
         'Task 3: Depression  1. You continue with your check-up. The patient has a long-standing history o...-e. Atypical antidepressants',
         '2. Which drugs have been escalated in dose at least twice? (Check all that apply.) -b. Sertraline',
         '2. Which drugs have been escalated in dose at least twice? (Check all that apply.) -c. Fluoxetine',
         '4. You’d like to know what date that provider changed the medication so you can investigate the n...'
         ]
#projection
tier3 = ['11. After asking the patient about his gout, he explains that he has not picked up his gout medic...',
         '2. The patient’s blood pressure did not decrease in the 3 years after he was prescribed the thiaz...',
         '4. What do you suspect happened with his new antihypertensive regimen of HCTZ + ACE inhibitor tha...',
         '5. Despite Mr. Smith’s diligent adherence to his exercise and diet regimen and his past medicatio...',
         '5. Why do you think the provider chose bupropion to prescribe in 2006? '
         ]
         
         
#Define a function to score each participant    
def returnScore(row,qlist):
    score=0
    for x in qlist:
        if '...' in x:
            metax = x.split('...',1)[0]+'...'
        elif '2. Which drugs have been escalated in dose' in x:
            metax = '2. Which drugs have been escalated in dose at least twice?\xa0(Check all that apply.)\xa0'
        else:
            metax = x
        if (row[x] in new.get(metax)):
            score+=1
    return(score)
    
tier1_control = cq_control.apply(lambda row: returnScore(row,tier1),axis=1)
tier1_interve = cq_interve.apply(lambda row: returnScore(row,tier1),axis=1)

tier2_control = cq_control.apply(lambda row: returnScore(row,tier2),axis=1)
tier2_interve = cq_interve.apply(lambda row: returnScore(row,tier2),axis=1)

tier3_control = cq_control.apply(lambda row: returnScore(row,tier3),axis=1)
tier3_interve = cq_interve.apply(lambda row: returnScore(row,tier3),axis=1)
    
