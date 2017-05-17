class A():
	def sum1(self,a,b):
		c = a+b
		return c
	
class B():
	def sub1(self,a,b):
		c = a-b 
		return c
		
class C(A,B):
	pass

c_obj = C()
print "Sum is ", c_obj.sum1(12,4)
print "After substraction ",c_obj.sub1(45,5)