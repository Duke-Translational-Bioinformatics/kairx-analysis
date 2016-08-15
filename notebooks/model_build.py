# Load modules and data
import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices

#read in our data
cq_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv","rb"))
cq_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv","rb"))

#Put data together for modeling
cq_interve['label'] = "intervention"
cq_control['label'] = "control"

final = pd.concat([cq_interve,cq_control])

final_df = final[['Score-sum','label','Q_TotalDuration']]
final_df_nm = final_df.dropna()

#Let's 

# Fit and summarize OLS model
mod = sm.OLS(spector_data.endog, spector_data.exog)
res = mod.fit()
print res.summary()


