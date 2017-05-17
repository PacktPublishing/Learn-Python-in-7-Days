import collections
employee = collections.namedtuple('emp','name, age, empid')

record1 = employee("Hamilton", 28, 12365 ) 

print "Record is ", record1
print "name of employee is ", record1.name
print "age of employee is ", record1.empid

print "type is ",type(record1)