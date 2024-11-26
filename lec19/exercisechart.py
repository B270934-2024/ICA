#!/bin/python3
#use the ecoli.txt file and, using the code above as a starting point, make a chart which shows the AT content in a sliding 1000 base window
#for the first 50000 bases
#for the first 100000 bases
#for the whole genome
import os, sys
import numpy as np
import matplotlib.pyplot as plt
eco=open("ecoli.txt").read().replace('\n','').upper()
window=-1
upperrange=-1
while window < 0 or window > len(eco):
    window = int(input("Please print the window size.\n"))
while upperrange < 0 or  upperrange > len(eco): 
    upperrange= int(input("Please print the size of the genome you want to read, up to "+str(len(eco))+'\n'))
atgc=""
while atgc != "AT" and atgc != "GC":
    atgc=input("AT or GC?").upper()
    
eco=open("ecoli.txt").read().replace('\n','').upper()[0:upperrange]
#int(input("Please print the window size."))
at=[]
for frame in range(len(eco)-window):
    win=eco[frame:frame+window]
    if atgc=="AT":
        at.append((win.count('A')+win.count('T'))/window)
    else:
        at.append(1-(win.count('A')+win.count('T'))/window)
plt.xlabel('Position on Genome')
plt.ylabel(atgc+' content Percentage')
plt.title('Window size of ' + str(window))
plt.plot(at,label=atgc,linewidth=3)
plt.savefig("chart.png",transparent=True)
plt.show()
