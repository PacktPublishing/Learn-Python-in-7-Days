def fun1(x):
	return x[1]

list_tup = [("a",4),("b",1),("v",5),("f",2)]
list_tup.sort(key= fun1)
print list_tup