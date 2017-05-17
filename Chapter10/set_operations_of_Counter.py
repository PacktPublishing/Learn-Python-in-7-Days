import collections

co1 = collections.Counter(['C','L','E','O','P','A','T','R','A'])
co2 = collections.Counter('JULIUS CAESAR')

print co1
print co2

print "addition \n",co1 + co2 # Prints addition of sets
print "Subtraction\n", co1 - co2 # Prints substration of sets

print "Union \n", co1 | co2 # Prints union of sets
print "Intersection \n", co1 & co2  # Prints intersection of sets