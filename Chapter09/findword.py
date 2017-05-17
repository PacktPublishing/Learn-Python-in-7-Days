word = raw_input("Enter the word  ")
word = word.lower()
file_txt = open("batman.txt", "r")

count = 0
for each in file_txt:
	if word in each.lower():
		count = count+1

print "The ", word ," occured ",count, " times"
		