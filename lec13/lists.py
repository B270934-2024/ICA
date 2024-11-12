#!/bin/python3
colour=['1']
#import pandas
#pandas.flatten can be used for joining strings together but really extend is what you wanna do.
#print(colour)
col = ['red','blue','green','red']
colours = "red,blue,green,red"
print(colours.split(','))
#wow a list wow
col.append('blue')
print(col)
#last position is [-1]
#penultimate is [-2]

#set(col) removes non redundants. Uses {} not [].

print(sorted(list(set(col))))
print(col)

print(list(range(10)))
#a list of numbers 1 to 10

#list methods
#list.append(item) : adds a single item to the end of the list
#list.insert(index, item) : inserts the item at the given index position, "moving" items to the right
#list.extend(list2) : adds the items in list2 to the end of the list. Using + or += on a list is similar to using extend()
#list.index(item) : searches for the given item from the start of the list and returns its index. Throws a ValueError if the item does not appear (use in to check without a ValueError)
#list.remove(item) : searches for the first instance of the given item and removes it (throws ValueError if not present)
#list.sort() : sorts the list in place; the sorted() function is probably better
#list.reverse() : reverses the list in place
#list.pop(index) : removes and returns the item at the given index, defaults to the rightmost item, a bit like the opposite of append()
import string
print(string.ascii_lowercase) #a string contianing all ascii lower case characters
tupletest=1,2,3,4,5,6,7,8,9,0
print(tupletest)
#tuples use () and are uneditable.
# Using join
#s='-'
#s.join(somecolours1)
#'green-red-blue'
#s='|'
#s.join(somecolours1)
#'green|red|blue'
#s=' then '
#s.join(somecolours1)
#'green then red then blue'
numbs=list(range(10))
somecolours1_and_numbs = col + list(''.join(str(e) for e in numbs))
print(somecolours1_and_numbs)
#As we must turn each number in the range into a string. didn't know you could have inline for loops
#every second item = [::2]
