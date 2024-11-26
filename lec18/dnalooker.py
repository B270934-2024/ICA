#!/bin/python3
import re
dna=open("long_dna.txt")
dnaline=dna.read()
dnaline=dnaline.rstrip("\n")
count=0
dnasplit=re.split(r"A(G|C|A|T)TAAT",dnaline) #single digest
dnasplit2=re.split(r"A[GCAT]TAAT",dnaline)
dnasplitsplit=re.split(r"(GC(A|G)(A|T)TG)|(A(G|C|A|T)TAAT)",dnaline) # second digest
dnasplitsplit2=re.split(r"(GC[AG][AT]TG|A[GCAT]TAAT)",dnaline)
print(len(dnaline))
print("After single digestion:")
#print("splitsplit")
#print(dnasplit2)
#print("split")
#print(dnasplit)
for seq in dnasplit2:
    if seq == None:
        continue
    else:
        print("#######################")
        count +=1
        if count % 2 == 0:
            length=len(seq)+3
            print("AAT"+seq)
        else:
            length=len(seq)+3
            print(seq+"ANT")
    print("Sequence "+str(count)+ " is "+str(length)+ " bases long.")
    print("#######################")
count=0
print("After double digestion:")
print("#######################")
for seq in dnasplitsplit2:
    count+=1
    if seq == None:
        continue
    else:
        print("#######################")
        if count % 2 == 0:
            length=len(seq)+2
            print("TG"+seq)#+"GCRW")
        else:
            length=len(seq)+4
            print(seq+"GCRW")
    print("Sequence "+str(count)+" is "+ str(length) + "bases long.")
    print("#######################")
#The above was a good attempt but basically it doesn't work. Its just worse than using find iter.
#Could also use find iter, then matching.start()+3 to find the start sites.
print(re.finditer(r"(GC(A|G)(A|T)TG)|(A(G|C|A|T)TAAT)", dnaline))

