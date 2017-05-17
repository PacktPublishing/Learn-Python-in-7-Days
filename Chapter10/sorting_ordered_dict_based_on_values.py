import collections 
print '\n Order dictionary'
d1 = collections.OrderedDict()
d1['a']= 'SAS'
d1['d']= 'PYTHON'
d1['b']= 'SAP HANNA'
d1['f']= 'R'
d1['c']= 'JULIA'

for k,v in d1.items():
	print k, ":",v
print '\n Sorted Order dictionary'
dict = collections.OrderedDict(sorted(d1.items(), key=lambda (k,v): v))

for k,v in dict.items():
	print k, ":",v