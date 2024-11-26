#!/bin/python3
import re
#prefix a string with 'r' to make it raw, and turn special characters into text. Basically adds another backslash.
dna = r'ATCGCGAATTCAC'
if re.search(r'(N|R|Y|S|W|K|M|B|D|H|V)',dna.upper()):
    print(dna.upper())
    print("yup something's wrong")
else:
    print("nothing's bad here")
    print(dna.upper())
#re.search will find the first instance of a pattern and return 'true' if found, or nothing, if not found.


#.group will collate the search result into what we actually find.

dna = 'ATCGCGYAATTCAC'
if re.search(r'[^GATC]', dna):
    print('Ambiguous base found!')
    match=re.search(r'[^GATC]',dna)
    print('Base is: '+match.group())
else :
    print('Sequence has no ambiguous bases in it.')

re.search(r'T.A',dna.upper())
#search for T[any]A
if re.search(r'^[AG]', 'TGTC') or re.search(r'T$', 'TGTC'):
    print('One condition met')
else :
    print('Neither condition met')



animals=['Homo sapiens', 'Mus musculus', 'Gorilla']
for animal in animals:
    if re.search(r' ',animal):
        arr=animal.split()
        print(animal + ': Genus: ' + arr[0] + ', Species: ' +arr[1])
    else:
        print(animal+ " is not in proper formatting!")


lots_of_animals=['a','homo sapiens', 'bufo bufo']
for this_animal in lots_of_animals :
   new_match_obj = re.search('(.+) (.+)',this_animal) #we search for two words
   if new_match_obj :
     print(this_animal + ': genus is ' + new_match_obj.group(1) + ', species is ' + new_match_obj.group(2))
   else :
     print('Unable to find a full genus and species pair for ' + this_animal)



#re.finditer() will find multiple matches and return objects for each.
#re.findall will find all things returning the list of found characters
#re.split will split around a regex
#also '?' means this might be requied - zero or one of a preceding string, or match everything enclosed. Also allows overlap - BLAST
stringlength=len(dna)
AorT_runs_v3 = re.finditer(r'(?=[AT]{3,3})', dna)
counter=0
for ATs in AorT_runs_v3:
    counter += 1
    run_start = ATs.start()
    run_end = run_start+stringlength
    print('A/T triplet (overlapping): ' +str(counter)+' extends from base ' \
    + str(run_start+1) \
    + ' to base ' +str(run_end)+' and has sequence ' +str(dna[run_start:run_end]))
print('The input sequence was ' + dna)
#This will find the number of triplets (3,3) with As and Ts only. 


