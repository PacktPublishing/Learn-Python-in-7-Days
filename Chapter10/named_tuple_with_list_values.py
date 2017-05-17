import collections
employee = collections.namedtuple('emp','name, age, empid')
list1 = ['BOB', 21, 34567]
record2 =employee._make(list1)
print record2
print "\n"
print (record2._asdict())