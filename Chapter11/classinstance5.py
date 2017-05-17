class Leapx_org():
	mul_num = 1.20
	count= 0
	def __init__(self,first,last,pay):
		self.f_name = first
		self.l_name = last
		self.pay_amt = pay 
		self.full_name = first+" "+last
		Leapx_org.count = Leapx_org.count+1
		#self.count = self.count+1
		print self.count
	def make_email(self):
		return self.f_name+ "."+self.l_name+"@xyz.com"
		
	def incrementpay(self):
		self.pay_amt = int(self.pay_amt*self.mul_num)
		return self.pay_amt
	
L_obj1 = Leapx_org('mohit', 'RAJ', 60000)
L_obj2 = Leapx_org('Ravender', 'Dahiya',70000) 
L_obj2 = Leapx_org('Bhaskar', 'DAS',70000)

print "Number of Employees are : ", Leapx_org.count