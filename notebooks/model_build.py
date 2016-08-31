# Load modules and data
import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices
import matplotlib.pyplot as plt

#read in our data
cq_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv","rb"))
cq_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv","rb"))

#Put data together for modeling
cq_interve['label'] = "intervention"
cq_control['label'] = "control"

final = pd.concat([cq_interve,cq_control])

final_df = final[['Score-sum','label','Q_TotalDuration']]
final_df_nm = final_df.dropna()
final_df_nm['Score'] = final_df_nm['Score-sum']

final_df_nm.head()
final_df_nm = final_df_nm[final_df_nm['Q_TotalDuration'] < 10000]

###############################################################################
#Model 1
###############################################################################
y, X = dmatrices('Score ~ label',data=final_df_nm, return_type='dataframe')

# Fit and summarize OLS model
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary())



###############################################################################
#Model 2
###############################################################################
#Let's use patsy to define our design matrix
y, X = dmatrices('Score ~ label + Q_TotalDuration',data=final_df_nm, return_type='dataframe')

# Fit and summarize OLS model
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary())


###############################################################################
#Model 3
###############################################################################
#Let's use patsy to define our design matrix
y, X = dmatrices('Score ~ label + Q_TotalDuration + label*Q_TotalDuration',data=final_df_nm, return_type='dataframe')

# Fit and summarize OLS model
mod = sm.OLS(y, X[['label[intervention]']])
res = mod.fit()
print(res.summary())


colors = ['red' if x=='intervention' else 'green' for x in final_df_nm['label']]

plt.scatter(final_df_nm['Q_TotalDuration'],final_df_nm['Score'],color=colors, alpha=0.5)


import matplotlib.patches as mpatches

classes = ['intervention','control']
class_colours = ['r','g']
recs = []
for i in range(0,len(class_colours)):
    recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))
plt.legend(recs,classes,loc=4)

X = [1,2,3,4]
Ys = np.array([[4,8,12,16],
      [1,4,9,16],
      [17, 10, 13, 18],
      [9, 10, 18, 11],
      [4, 15, 17, 6],
      [7, 10, 8, 7],
      [9, 0, 10, 11],
      [14, 1, 15, 5],
      [8, 15, 9, 14],
       [20, 7, 1, 5]])
nCols = len(X)  
nRows = Ys.shape[0]

colors = matplotlib.cm.rainbow(np.linspace(0, 1, len(Ys)))

cs = [colors[i//len(X)] for i in range(len(Ys)*len(X))] #could be done with numpy's repmat
Xs=X*nRows #use list multiplication for repreating
matplotlib.pyplot.scatter(Xs,Ys.flatten(),color=cs)


n = 100
r = 2 * np.random.rand(n)
theta = 2 * np.pi * np.random.rand(n)
area = 200 * r**2 * np.random.rand(n)
colors = theta

