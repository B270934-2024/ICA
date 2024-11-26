#!/bin/python3
import re,os,subprocess as sp
#sp.call("esearch -db 'nuccore' -query 'AJ223353[Accession]' | efetch -format fasta > AJ223353.nuc.fa",shell=True)
#sp.call("esearch -db 'nuccore' -query 'AJ223353[Accession]' | efetch -format genbank > AJ223353.nuc.gen",shell=True)

txt=open("plain_genomic_seq.txt")
fst=open("AJ223353.nuc.fa")
output=open("output.txt","a")
contents=fst.read()        
contents=contents.split()
aj223353=[]
text=txt.read()
#text=text.split()
#{29:409}


output.write("\n>AJ223353 coding section\n")
for string in contents:
    if len(string) > 12:
        output.write(string)
        aj223353.append(string)

aj223353=''.join(aj223353)
print("Coding sequences of AJ223353: "+aj223353[28:409])
output.write(aj223353[28:409])
print("Intron sequences of AJ223353: "+aj223353[409:])
output.write("\n>AJ223353 non-coding section\n")
output.write(aj223353[409:])
#print("Coding sequences of Genomic Sequence: "+text.replace("X","").upper())
z=-1
#re.sub"[]"
stuffwedontwant=re.sub("[GCATgcat]","",text)
stuffwedontwant=list(stuffwedontwant)
stuffwedontwant=set(stuffwedontwant)
text=list(text)
#print(text)
for x in text:
    z+=1
    for y in stuffwedontwant:
       if x == y:
           text[z]=""

print(''.join(text).upper())
fst.close
output.close
txt.close
