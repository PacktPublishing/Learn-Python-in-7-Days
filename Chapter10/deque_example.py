import collections 

de = collections.deque('India')
print 'deque:', de
print 'Lenght :', len(de)
print 'left end:', de[0]
print 'right end:', de[-1]

de.remove('a')

print 'After removing:', de