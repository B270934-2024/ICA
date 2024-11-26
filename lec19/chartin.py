#!/bin/python3
import os, sys
import numpy as np
import matplotlib.pyplot as plt

#plt.plot([1,5,6,8,4,6,7,30,1,2,6,4,9,8,1])
#plt.savefig("Chart_01.png",transparent=True)
#plt.show()
#plt.close()
#plt.plot plots numbers wow yay

numbers =[1,5,6,8,4,6,7,3,1,2,6,4,9,8,1]
#plt.plot(numbers, color="red", label="My numbers")
#plt.legend(loc='upper right')
#plt.xlabel('Xvalues')
#plt.title('a matlpotlib chart')
#plt.savefig("Chart_03.png",transparent=True)
#plt.show()

#can plot any number of things. I.e.:

more_numbers = [8,9,1,2,6,4,8,6,5,8,4,3,5,4,3]
plt.plot(numbers,color="red",label="mynum")
plt.plot(more_numbers,color="blue",label="morenum")
plot.legend()
plt.figure(figsize=(20,10)) # set the size of the figure, default is dots per inch
plt.savefig("chart04.png",transparent=True)
plt.show()

#default is plotting on Y axis

x = np.linspace(0, 20, 1000)
#1000 equally spaced numbers between 0 and 20
y = np.sin(x)
plt.plot(x,y)
plt.savefig("chart05.png",transparent=True)
# 'r' = red
# 'g' = green
# 'b' = blue
# 'c' = cyan
# 'm' = magenta
# 'y' = yellow
# 'k' = black
# 'w' = white
# '-'  = solid
# '--' = dashed
# ':'  = dotted
# '-.' = dot-dashed
# '.'  = points
# 'o'  = filled circles
# '^'  = filled triangles
# 's'  = filled squares
#iteration from 0 to 5 (stops at 4.8), interval 0.2
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--',     t, t**2, 'bs',     t, t**3, 'g^')
#plot t on x, followed by:
#t on y, in red, with dashed line.
#t on x, t^2 on y,blue, filled squares
#t on x, t^3 on y, green, filled triangles
plt.savefig("chart05.png",transparent=True)
plt.show()

#properties of lines:
plt.plot(x, y, linewidth=2.0)
a = x+2
b = y*5
line1, line2 = plt.plot(x, y, a, b)
plt.setp(line1, color='r', linewidth=6.0)
plt.setp(line2, color='b', linewidth=2.0)
plt.savefig("Chart_77.png",transparent=True)
plt.show()
#this produces the sin curve from above, but with a thick red line (y*5) and a thin blue line (x+2)


#multi-plot drifting
#subplot(211) is identical to subplot(2, 1, 1) and means 2 rows, 1 column, first panel.
#numrows,
#numcols,
#fignum
def f(t):
    return np.exp(-t) * np.cos(2* np.pi *t)
#just a mathemetical function.
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#now on to plot 2, out of 2 rows and 1 column this is figure 2.
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.xlabel('X axis values')
plt.ylabel('Y axis values')
#the above applies to only this.
plt.savefig("Chart_08.png",transparent=True)
plt.show()

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
#x is now a bunch of random numbers multiplied by sigma, + mu
#set n, bins, and patches to 3 values that come out of this histogram
n, bins, patches = plt.hist(x, 50, density=True, facecolor='#ee42f4', alpha=0.75)
#n: is the number of counts (normally!) in each bin of the histogram, this time it is density
#bins: is the left hand edge of each bin
#patches: the individual patches used to create the histogram, e.g a collection of rectangles
#facecolor: what colour do we want? can use hex values

plt.xlabel('IQ values')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.axis([40, 160, 0, 0.03]) # axis in range x1:x2, y1:y2
plt.text(60, .025, r'$\mu=100,\ \sigma=15$') #add on a label with special characters mu and sigma, size 60, etc.
plt.axvline(x=mu+(2*sigma),linewidth=4, color='r') # also plot a line on it that's red, width 4, at point 2sigma+mu
plt.text(mu+(2.1*sigma), .025, r'$\mu + 2\sigma$') #label that line
plt.grid(True)
plt.savefig("Chart_11.png",transparent=True)
plt.show()

#annotate()


t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2* np.pi *t)
line = plt.plot(t, s, lw=2)
#a cos (2pi*t) wave.
for peak in range(1,5):
   plt.annotate('Pointy bits', xy=(peak, 1), xytext=(2.5, 1.5),
            arrowprops=dict(facecolor='#42f442', shrink=0.05), # also have horrific green arrows pointing.
            )
#the above will label where y = 1, the max value on the plot

plt.ylim(-2,2) # set limits of y, duh.


# LOG SCALES
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y=y.sort()
x = np.arange(len(y))
plt.figure(figsize=(20,10))
plt.subplot(221)
plt.plot(x, y, 'r-',linewidth=3.0)
plt.yscale('linear')
plt.title('LINEAR')
plt.grid(True)
#a red line on plot 1 of up to 4.
plt.subplot(222)
plt.plot(x, y, 'g-',linewidth=3.0)
plt.yscale('log')
plt.title('LOG')
plt.grid(True)
#green line on log
plt.subplot(223)
plt.plot(x, y - y.mean(), 'm-',linewidth=3.0)
plt.yscale('symlog', linthreshy=0.05)
plt.title('SYMLOG')
plt.grid(True)
#symmetric log, y minus the mean of y
plt.subplot(224)
plt.plot(x, y, 'b-',linewidth=3.0)
plt.yscale('logit')
plt.title('LOGIT')
plt.grid(True)
#log-odds

#built in functions that are in the yscale command. There's also xscale.

#doing this from a file:
ecoli = open("ecoli.txt").read().replace('\n', '').upper()[0:100000]
#open the file ecoli.txt replcae '\n's with '', and then do this for the first 100,000 lines
window = 1000
#this is the reading frame. Then, we make 4 arrays to hold each base value.
a=[]
c=[]
g=[]
t=[]
#this iterates over the entire thing, with the frame 1000, looking at a thousand bases at a time.
for start in range(len(ecoli) - window):
    win = ecoli[start:start+window]
    a.append(win.count('A') / window)
    t.append(win.count('T') / window)
    g.append(win.count('G') / window)
    c.append(win.count('C') / window)
#then we append each of the counts to our arrays as a percentage of the sliding window.
plt.figure(figsize=(20,10))
plt.plot(a, label="A")
plt.plot(t, label="T")
plt.plot(g, label="G")
plt.plot(c, label="C")
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.legend()
#then we start plotting!
plt.savefig("Chart_15.png",transparent=True)
plt.show()

#What if we wanted to find dinucleotides specifically?
ecoli = open("ecoli.txt").read().replace('\n', '').upper()[0:100000]
#once again.
window = 1000
aa = []
tt = []
gg = []
cc = []
counter =0
for start in range(len(ecoli) - window):
    counter+=1
    print(counter)
    win=ecoli[start:window]
    aa.append(win.count('AA') / win.count('A'))
    tt.append(win.count('TT') / win.count('T'))
    gg.append(win.count('GG') / win.count('G'))
    cc.append(win.count('CC') / win.count('C'))

#print counter to the screen. then we look at the dinucleotides as a percentage of the total concentration of the substance.
#then, we plot this! 4 times!
plt.figure(figsize=(20,10))
plt.subplot(221)
plt.plot(aa, label="AA rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()
plt.subplot(222)
plt.plot(tt, label="TT rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()
plt.subplot(223)
plt.plot(gg, label="GG rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()
plt.subplot(224)
plt.plot(cc, label="CC rep")
plt.ylabel('Overrepresentation')
plt.xlabel('Position on genome')
plt.legend()
plt.savefig("Chart_16.png",transparent=True)
plt.show()

#we can also just adjust window size...





