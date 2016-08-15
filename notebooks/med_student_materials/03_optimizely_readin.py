import pandas as pd
import re

cases = pd.read_table(open('/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/optimizely_data/6260120514.txt','r'),
                        parse_dates=['timestamp'])
control = pd.read_table(open('/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/optimizely_data/6281421834.txt','r'),
                        parse_dates=['timestamp'])

###################################################
###################################################
#Need to merge to find how many we can match by IPV4

control[~control.user_ip.str.contains(':')].head(n=20)
control_ipv4 = conrol[user_id]
c_gb = control.groupby('user_id')

cq_control = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Control.csv","rb"))
cq_interve = pd.read_csv(header=1,filepath_or_buffer=open("/Users/nn31/Dropbox/40-githubRrepos/kairx-analysis/notebooks/med_student_materials/qualtrics_data/KaiRx_Clinical_Questionnaire__Intervention.csv","rb"))
