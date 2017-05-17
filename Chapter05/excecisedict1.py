list1 = [1,2,3,4,5]
list2 = ["a", "b", "c","d", "e"]
dict1 = {}
for index1 in xrange(len(list1)):
	dict1[list1[index1]] = list2[index1]
print dict1