#!/bin/python3
#open, read, close!
import os,shutil,subprocess,sys
myFile=open("myDNA.txt") # a file object, containing the data enclosed in myDATA.txt
#print(myFile.read()) # prints the entire file. Uses new lines as new lines. REMEMBER THAT READ ONLY WORKS ONCE
#We generally want to remove the end line characters.
#We do this by first....
contents=myFile.read() #this is a string, each line ends with '\n'. 
myDNA1=contents.rstrip("\n") # this removes '\n'.
#can also, as contents is just a string...
contents=contents.replace("\n","")
#or....
contents=contents.split()
#now its a list!
myFile.close()

#W - write
#R - read
#A - append
output=open("out.txt","w")
output.write("Igot95Percentwoo")
output.close()




#A better way is:
#with open ("myDNA.txt","A") as myFile:
#   myFile.write("AAAAAAA") this will append that line onto the DNA sequence.


#But what about pathing?????
#here's where we import os.
#os.getcwd() == pwd
#os.chdir() == cd
#os.environ('HOME') ==${HOME}
#os.listdir() == ls, automatically as a list.
#os.rename == mv
#os.mkdir == mkdir
#os.system("ls -al") == ls -al
#os.remove() == rm
#os.rmdir() == rm -d

#We also throw in import shutil
#This lets us use filetrees
#i.e., 
#shutil.copy("original","copy") - basically cp.
#shutil.copytree("original_directory","copydirectory")
#shutil.rmtree() = rm -d-f

#We ALSO throw in subprocess
#This is normally for shell stuff.
#subprocess.\t\t will give us some info.
#mycal = subprocess.check_output("cal").decode("utf-8") will give a calender using \n to separate lines and like, actually do them, as we specify utf-8 encoding.


#How do we get input from the command line????
#sys.argv[x], starting at 1.

#fpipe = open("MyFruityScript.py","w") # pretty sure you'd need to append.
#We can write using the interpreter by repeatedly going e.g., fpipe.write("BLAHBLAHBLAH\n")




#We can actually run shell from within python
#subprocess.call("chmod 700 MyFruityScript.py", shell=True)
#subprocess.call("./MyFruityScript.py apples lychees", shell=True) <- that seems like a really easy way to crash the computer if you put it in a loop lol. 

