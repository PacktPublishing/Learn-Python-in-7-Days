class A():
	def sum1(self,a,b):
		c = a+b
		return c
	
class B(A):
	def sub1(self,a,b):
		c = a-b 
		return c
		
class C(B):
	pass

c_obj = C()
print "Sum is ", c_obj.sum1(12,4)
