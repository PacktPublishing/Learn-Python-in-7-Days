class Leapx_org():
	mul_num = 1.20
	mul_num2 = 1.30
	def __init__(self,first,last,pay):
		self.f_name = first
		self.l_name = last
		self.pay_amt = pay 
		self.full_name = first+" "+last
	@staticmethod
	def check_amt(amt):
		if amt <50000:
			return True
		else :
			return False
	def incrementpay(self):
		if self.check_amt(self.pay_amt):
			self.pay_amt = int(self.pay_amt*self.mul_num2)
		else :
			self.pay_amt = int(self.pay_amt*self.mul_num)
		return self.pay_amt

		

L_obj1 = Leapx_org('mohit', 'RAJ', 40000)
L_obj2 = Leapx_org('Ravender', 'Dahiya',70000)
L_obj1.incrementpay()
L_obj2.incrementpay()
print L_obj1.pay_amt
print L_obj2.pay_amt