def infocity(**var):
	print var
	for key, value in var.items():
		print "%s == %s" %(key,value)
 

infocity(name="l4w", age = 20, city="Los Angeles")
infocity(name="John",age=45, city="London", sex="male", medals=0)