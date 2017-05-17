list1 = [1,2,4,5,1,1,4,1,56]
list2 = []
for i in xrange(len(list1)):
	if list1[i]==1:
		list2.append(i)
print list2

print [i for i in xrange(len(list1)) if list1[i]==1 ]