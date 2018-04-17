# -*- coding: utf-8 -*-
"""
Created on Sun Mar 04 19:22:28 2018
Within our group we each took one of the tables, Felicia provided the code for the 
first table, Robinson provided the code for the second table, and Elijah provided 
the code for the third table

@author: Fe
"""
import pandas as pd 
import csv 
import numpy as np
import matplotlib.pyplot as plt
#header
print "70-511, Spring 2018"
print "Group #18"
print "Felicia Cobb, Elijah Malloy Robinson Mikowlski"
print "Programming Assignment #7" 
print ""
#function 
def get_stats(group):
    return{ 'mean': group.mean(),
           'count':group.count(),
            'std': group.std(),
            'min': group.min(),
            'max':group.max(),
            'sum':group.sum()
                } 

#input for tables
input_file = pd.read_csv('ss13hil.csv')
df=pd.read_csv('ss13hil.csv')

#table #1
df1 = pd.DataFrame(input_file['HHT'])
df1['HHT']=df1['HHT'].apply(str)
df1['HHT'].replace(['1.0','2.0','3.0','4.0','5.0','6.0','7.0'], 
                     ['Married couple household',
                      'Other family household:Male householder, no wife present',
                      'Other family household:Female householder, no husband present',
                      'Nonfamily household:Male householder:Living alone',
                      'Nonfamily household:Male householder:Not living alone',
                       'Nonfamily household:Female householder:Living alone', 
                       'Nonfamily household:Female householder:Not living alone'],inplace=True)                                 
df2 = pd.DataFrame(input_file['HINCP'])
dfmerge= df1.merge(df2,left_index=True,right_index=True)
dfmerge.dropna(axis=0, how='any', inplace=True)
group = dfmerge['HINCP'].groupby(dfmerge['HHT'])
dfmerge.set_index('HHT',inplace=True)
print "*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***"
group_stats1 = group.apply(get_stats).unstack()   
group_stats1.sort_values(by='mean',ascending=False,inplace=True)
group_stats1.index.names = ['HHT - Household/family type'] 
group_stats1 = group_stats1[['mean','std','count','min','max']]
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 800)
print group_stats1   
print ""

#table #2
print "*** Table 2 - HHL vs. ACCESS - Frequency Table ***"
df=df.dropna(subset=['HHL','WGTP','ACCESS'],how='any')
df=pd.concat([df['HHL'],df['WGTP'],df['ACCESS']],axis=1)
total=sum(df['WGTP'])
df['HHL']=df['HHL'].replace(1.0, 'English Only')
df['HHL']=df['HHL'].replace(2.0, 'Spanish')
df['HHL']=df['HHL'].replace(3.0, 'Other Indo-Europeon Language')
df['HHL']=df['HHL'].replace(4.0, 'Asian and Pacific Island Languages')
df['HHL']=df['HHL'].replace(5.0, 'Other Language')
df_sums=df.groupby(['HHL','ACCESS'], as_index=False).sum()
df_new=pd.pivot_table(df_sums, values='WGTP', index=['HHL'],
                   columns=['ACCESS'])
df_new['All']=df_new.sum(axis=1)
All=df_new.sum().tolist()
df_new.loc['All'] = All
df_new=df_new/total
df_new.columns=['Yes, w/ Subsrc.','Yes, wo/Subsrc.','No','All']
df_new['Yes, w/ Subsrc.']=pd.Series(["{0:.2f}%".format(val*100) for val in df_new['Yes, w/ Subsrc.']],index=df_new.index)
df_new['Yes, wo/Subsrc.']=pd.Series(["{0:.2f}%".format(val*100) for val in df_new['Yes, wo/Subsrc.']],index=df_new.index)
df_new['No']=pd.Series(["{0:.2f}%".format(val*100) for val in df_new['No']],index=df_new.index)
df_new['All']=pd.Series(["{0:.2f}%".format(val*100) for val in df_new['All']],index=df_new.index)
print df_new
print ""

#quantile analysis- table #3
print "*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***"
df6= pd.DataFrame(input_file['HINCP'])
df6.dropna(axis=0, how='any', inplace=True)
grouping = pd.qcut(df6.HINCP,3,labels=['low', 'medium', 'high'])
grouped=df6.HINCP.groupby(grouping)
group_stats2=grouped.apply(get_stats).unstack()
group_stats2.iloc[:,3] = group_stats2.iloc[:,3].astype(int)
group_stats2.iloc[:,1] = group_stats2.iloc[:,1].astype(int)
group_stats2=group_stats2[['min','max','mean']]
df7=pd.DataFrame(input_file['WGTP'])
w_grouping=pd.qcut(df7.WGTP,3,labels=['low','medium','high'])
w_grouped=df7.WGTP.groupby(w_grouping)
w_grouped_stats=w_grouped.apply(get_stats).unstack()
group_stats2['household_count']= w_grouped_stats[['sum']].astype(int)
print group_stats2

