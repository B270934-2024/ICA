#!/bin/python3
import os,sys,numpy
import subprocess as sp
import pandas as pd

#subprocess.call("pip3 install pandas", shell = True)
x=pd.Series(['a','b','c','d'])
y=pd.Series([1,2,3,4])
print(pd.DataFrame( { 'letter':x,'number':y  } ))
#sp.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)
#download the data

#the series statements...
#create 2 different kinds of lists aligned with eachother

#euk=pandas.read_csv('eukaryotes.txt',sep="\t")
#euk.columns lets us know what the headers are, df.shape tells us how big it is, rows x columns. Can slice bits out with euk[3:7] or head() or tail() or euk.describe

#oh! but there's some N/A values! So instead we change our original read line by adding...
euk=pd.read_csv('eukaryotes.txt',sep="\t",na_values=['-'])
print(euk.describe()) #just summary() in R
print(euk['#Organism/Name'] == 'Arabidopsis thaliana') 
euk[euk['#Organism/Name'].isin(['Arabidopsis thaliana'])].shape
Ara = euk[euk['#Organism/Name'] == 'Arabidopsis thaliana']
print(Ara)
#Apply lets us change strings.
Ara.apply(lambda x : x['#Organism/Name'].upper(), axis=1).head()
#We need lambda here: lambda just means do this function to x. Here, it finds the name and turns it into upper case.
Ara.to_csv("Arabidopsis_Only.tsv",sep="\t",header=True)
#Can look into the file system: euk['#Organism/Name#'].value_counts()
#generally use head.
#euk['#Organism/Name']
print(euk[euk.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds'], axis=1 )].shape[0])

birdMammal=euk[euk.apply( lambda x : x['Size (Mb)'] < 500 and x['SubGroup'] in ['Birds','Mammals'],axis=1)]
print(birdMammal.shape)
#if X is smaller than 500mb and is a bird or mammal,save it to birdMammal, a new data frame. Axis=1 forces it to go vertical
#Who has the largest genome?
print(birdMammal.sort_values('Size (Mb)',ascending=False).head())
#Sort it through via the size column, looking at descending order
#In addition, head() will return a new dataframe that's 5 rows long. to make it stick...
print(birdMammal.sort_values('Size (Mb)',ascending=False,inplace=True))
#euk.sort_values(['#Organism/Name', 'GC%'], ascending=[True, False]).head()
#This will sort by name, then within names that are close enough, will sort by GC% count
birdMammal['AT_content'] = 100 - (birdMammal['GC%'])
birdMammalSort = birdMammal.sort_values(['#Organism/Name'],ascending=True,inplace=True)
birdMammal.to_csv("birdmammal.tsv",sep="\t",header=True)
#this appends an AT content column to the database.
#can use mean, median, mode, corr(), std(), etc.

#lets read a small section
df_mini = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='Assembly Accession').head()
#this uses Assembly Accession as our primary key.
df_center = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'], index_col='Center')
#this uses center as it. Will exclude the column we select from this


#df.iloc[0:5]                 # first five rows of dataframe
#df.iloc[:, 0:2]              # first two columns of data frame with all rows
#df.iloc[ [0,3,6,24], [0,5,6] ] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
#df.iloc[0:5, 5:8]            # first 5 rows and 5th 6th 7th columns

#data.loc[<row selection>, <column selection>]
#df.loc['Glycine max (SAMN00002965)']
#search for name ^, will return all results with that.
#df.loc[ ['Glycine max (SAMN00002965)','Solanum lycopersicum (SAMN02981290)'] ]
#find 2 at once.

#df.loc[ ['Glycine max (SAMN00002965)','Solanum lycopersicum (SAMN02981290)'],['TaxID','Size (Mb)','GC%','Genes'] ]
#find those specific columns.


#df.groupby('#Organism/Name').mean()

#df.groupby('#Organism/Name').mean().iloc[0:14:,0:3]
#shows the mean of each species together, of rows 0:14 and columns 0:3



