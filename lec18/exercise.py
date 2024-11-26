#!/bin/python3
import re
accessionlist=['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
#contain the number 5
#contain the letter d or e
#contain the letters d and e in that order
#contain the letters d and e in that order with a single letter between them
#contain both the letters d and e in any order
#start with x or y
#start with x or y and end with e
#contains any 3 numbers in any order
#contains 3 different numbers in the accession
#contain three or more numbers in a row
#end with d followed by either a, r or p
print(accessionlist)

print("Contains the number 5:",end=" ")
for accession in accessionlist:
    if re.search(r'5',accession):
        print(accession,end=' ')
print("\n")
print("contains D or E:",end=" ")
for accession in accessionlist:
    if re.search(r'd|e',accession):
        print(accession,end=' ')
print("\n")
print("contains D then E:",end=" ")
for accession in accessionlist:    
    if re.search(r'de',accession):
        print(accession,end=' ')
print("\n")
print("contains D letter E:",end=" ")
for accession in accessionlist:    
    if re.search(r'd[a-zA-Z]e',accession):
        print(accession,end=' ')
print("\n")

print("contains D and E in any order:",end=" ")
for accession in accessionlist:
    if re.search(r'(d.*e|e.*d)',accession):
        print(accession,end=' ')
print("\n")
print("starts with X or Y:",end=" ")
for accession in accessionlist:
    if re.search(r'^(x|y)',accession):
        print(accession,end=' ')
print("\n")
print("starts with X or Y and ends in E:",end=" ")
for accession in accessionlist:
    if re.search(r'^(x|y).*e$',accession):
        print(accession,end=' ')
print("\n")
print("Contains any 3 numbers in any order",end=" ")
for accession in accessionlist:
    if len(re.findall(r'[0-9]',accession)) == 3:
        print(accession,end=" ")
print("\n")
print("Contains 3 different numbers in a row",end=" ")
for accession in accessionlist:
    if len(re.findall(r'[0-9]',accession)) >= 3:
        if len(set(re.findall(r'[0-9]',accession))) == 3:
            print(accession,end=" ")
print("\n")
print("Contains 3 or more numbers in a row",end = " ")
for accession in accessionlist:
    if re.search(r'[0-9]{3,}',accession):
        print(accession,end=" ")
print("\n")
print("end with d followed by a, r, or p",end=" ")
for accession in accessionlist:
    if re.search(r'd(a|r|p)$',accession):
        print(accession,end=" ")
print("\n")
print("contains D wildcard E:",end=" ")
for accession in accessionlist:
    if re.search(r'd.e',accession):
        print(accession,end=' ')

