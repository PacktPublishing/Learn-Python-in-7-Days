import collections
employee = collections.namedtuple('emp','name, age, empid')

record1 = employee("Marina", 28, 12365 ) 

print "Record is ", record1
print "\n"
print  record1._replace(age= 25)
print "\n"
print "Record is ", record1
print "\n"
record1 = record1._replace(age= 25)
print "Record is ", record1
