# Abdullah Al Mamun
# amamun@u.rochester.edu

import string
import random
from hashmap import hashMap


def key_gen(size=5, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(4))

#double value generator
def value_gen(size=5, chars=string.digits):
	return random.uniform(1.1,2000.3454353453)

#Initiatin two lists to store the keys and values
keyList = list()
valueList = list()

for i in range(800):
	keyList.append(key_gen())

for i in range(800):
	valueList.append(value_gen())

#Initiating the HashMap
DoubleHash = hashMap(870)

print "Printing size of DoubleHash"
print DoubleHash.getSize()
print ""
for i in range(800):
	DoubleHash.set(keyList[i],valueList[i])

print "Printing a value using the get function"
print DoubleHash.get(keyList[80])
print ""

print "Deleting a value using the delete function"
print DoubleHash.delete(keyList[80])
print ""

print "Showing that the value doesn't exist there anymore after deleting"
print DoubleHash.get(keyList[80])
print ""

print "Printing load factor"
print DoubleHash.load()
