# Abdullah Al Mamun
# amamun@u.rochester.edu

import string
import random
from hashmap import hashMap


def key_gen(size=5, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for _ in range(4))

#string value generator
def stringV_gen(size=5, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(5))

#integer value generator
def intV_gen(size=5, chars=string.digits):
	return (int)(''.join(random.choice(chars) for _ in range(5)))

#double value generator
def doubleV_gen(size=5, chars=string.digits):
	return random.uniform(1.1,2000.3454353453)

#Initiatin four lists to store the keys and the different types of values
keyList = list()
stringList = list()
intList = list()
doubleList = list()

#key generation
for i in range(800):
	keyList.append(key_gen())

#value generation
for i in range(800):
	stringList.append(stringV_gen())
for i in range(800):
	intList.append(intV_gen())
for i in range(800):
	doubleList.append(doubleV_gen())

#Initiating the HashMap
MixHash = hashMap(870)

print "Printing size of MixHash"
print MixHash.getSize()
print ""

for i in range(225):
	MixHash.set(keyList[i],stringList[i])
for i in range(225,450):
	MixHash.set(keyList[i],intList[i])
for i in range(450,675):
	MixHash.set(keyList[i],doubleList[i])


print "Printing a value using the get function"
print MixHash.get(keyList[50])
print ""

print "Deleting a value using the delete function"
print MixHash.delete(keyList[10])
print ""

print "Showing that the value doesn't exist there anymore after deleting"
print MixHash.get(keyList[10])
print ""

print "Printing load factor"
print MixHash.load()
