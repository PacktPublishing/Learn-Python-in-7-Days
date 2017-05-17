list1 = ["Blood sweat and respect\n",
		"The first two you give\n"
		"The last you earn\n"
		"Give it Earn it"]
text_file = open("wwerockquotes.txt", 'w') 
text_file.writelines(list1)
text_file.close()