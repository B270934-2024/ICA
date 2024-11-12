#!/bin/python3
#read the file 
#separate based upon commmas
#print all genes from melanogaster or simulans 
import re
csv=open("data.csv")
flies=csv.read()
#print(flies)
i=0
#flies=flies.rstrip("\n")
print(flies)
#for words in flies:
#   i+=1
#   print(words)
#   if words=="Drosophila melanogaster":
#        print("Drosophila melanogaster gene found ",end="containing: ")
#        print(words[i])
#   elif words=="Drosophila simulans":
#        print("Drosophila simulans gene found ",end="containing: ")
#        print(words[i])

