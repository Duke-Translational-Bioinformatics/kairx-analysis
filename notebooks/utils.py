# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:13:33 2016

@author: nn31
"""
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

colors = ['b','r','c','m','y','k']

def createBarPlot(questionsName,dd_number,question_choi,cq_control,cq_interve):
    #using this information, let's draw our bar plot
    length = len(question_choi[dd_number])
    depths = [[0,0] for i in range(length)]
    #Add actual data
    counts_control = cq_control[questionsName].value_counts(dropna=False)
    counts_interve = cq_interve[questionsName].value_counts(dropna=False)
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