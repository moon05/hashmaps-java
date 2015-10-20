# Abdullah Al Mamun
# amamun@u.rochester.edu

import string
import random
from hashmap import hashMap

def key_gen(size=5, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(7))

#string value generator
def value_gen(size=5, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(5))

#Initiatin two lists to store the keys and values
keyList = list()
valueList = list()

for i in range(800):
	keyList.append(key_gen())

for i in range(800):
	valueList.append(value_gen())

#Initiating the HashMap
StringHash = hashMap(870)

print "Printing size of StringHash"
print StringHash.getSize()
print ""
for i in range(800):
	StringHash.set(keyList[i],valueList[i])

print "Printing a value using the get function"
print StringHash.get(keyList[235])
print ""

print "Deleting a value using the delete function"
print StringHash.delete(keyList[235])
print ""

print "Showing that the value doesn't exist there anymore after deleting"
print StringHash.get(keyList[235])
print ""

print "Printing load factor"
print StringHash.load()

