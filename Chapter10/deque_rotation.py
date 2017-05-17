import collections

d = collections.deque(xrange(6))
print "Normal queue", d

d.rotate(2)
print "\nRight rotation :", d

d1 = collections.deque(xrange(6))
d1.rotate(-2)
print "\nleft rotation :", d1