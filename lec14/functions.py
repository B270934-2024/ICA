#!/bin/python3
def ATanalysis(myDNA,x=3): # Can also use file.read as input even, and more importantly, here you can SET DEFAULT VALUES!
    length=len(myDNA)
    myDNA=myDNA.upper()
    a_count=myDNA.count('A')
    t_count=myDNA.count('T')
    atper=(a_count+t_count)/length
    atper = round(atper,x)
    return atper
#Remember that you can always improve this. Just because it runs with no errors doesn't make it useful.

#Remember not to write functions that rely on external variables.
#First return line executed acts as an 'exit from function, providng this value as the output'
#basically break for functions.
#ALWAYS RETURN VALUES! or we can't make them generic, people wont know whats up.

#try :
#  get_at_content_v3("ATGCGTATtttTGAGCA")
#except :
#  f'Nah, ya broke it, numpty!'
#
#assert round(add_two_numbers(1.01, 2.01),2) == 3.02
#Assert asks in one line if something is the case. Will return a boolean value. Also python can't handle floats great and will mess up the calculations without round().

def Aminoanalysis(myprot,acid): # Can also use file.read as input even, and more importantly, here you can SET DEFAULT VALUES!
    length=len(myprot)
    acid=acid.upper()
    myprot=myprot.upper()
    acid_count=myprot.count(acid)
    acidper = round((acid_count/length),3)
    return acidper

def Aminoanalysislist(myprot,acid=['A','I','L','M','F','W','Y','V']):
    length=len(myprot)
    acid=list(''.join(acid).upper())
    myprot=myprot.upper()
    acid_count=[]
    acidper=[]
    x=0
    for code in acid:    
        acid_count.append(myprot.count(code))
        acidper.append(round((acid_count[x])/length,3))
        x+=1
    return acidper

def baseCount(seq):
    length=len(seq)
    seq=seq.upper()
    Acount=seq.count('A')
    Tcount=seq.count('T')
    Gcount=seq.count('G')
    Ccount=seq.count('C')
    tot=Acount+Tcount+Gcount+Ccount
    per=tot/length
    perunknown=1-per
    return round(perunknown,3)

print(baseCount("ATCGX"))




#print(Aminoanalysis("MSRSLLLRFLLFLLLLPPLP","Y"))
#print(Aminoanalysis("MSRSLLLRFLLFLLLLPPLP","M"))
#print(Aminoanalysislist("MSRSLLLRFLLFLLLPPPLP"))
#print(Aminoanalysislist("MSRSLLLRFLLFLLLPPPLP",["M"]))
#assert round(Aminoanalysis("MSRSLLLRFLLFLLLLPPLP","M") == round(5)
#assert round(Aminoanalysis("MSRSLLLRFLLFLLLLPPLP","r" == round(10)
#assert round(Aminoanalysis("MSRSLLLRFLLFLLLLPPLP","L") == round(50)
#assert round(Aminoanalysis("MSRSLLLRFLLFLLLLPPLP","Y") == round(0)
