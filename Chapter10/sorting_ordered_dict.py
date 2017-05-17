import collections 
print '\n Order dictionary'
d1 = collections.OrderedDict()
d1['a']= 'SAS'
d1['d']= 'PYTHON'
d1['b']= 'JULIA'
d1['f']= 'R'
d1['c']= 'SPARK'

for k,v in d1.items():
	print k, ":",v
print '\n Sorted Order dictionary'
dict = collections.OrderedDict(sorted(d1.items()))

for k,v in dict.items():
	print k, ":",v