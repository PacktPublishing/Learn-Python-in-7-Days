import collections 
print 'Regular Dictionary'
d = {}
d['a']= 'SAS'
d['b']= 'PYTHON'
d['c']= 'R'

for k,v in d.items():
	print k, ":",v
	
print '\n Ordered dictionary'

d1 = collections.OrderedDict()
d1['a']= 'SAS'
d1['b']= 'PYTHON'
d1['c']= 'R'

for k,v in d1.items():
	print k, ":",v