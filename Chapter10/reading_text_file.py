import collections

co = collections.Counter()
file_txt = open("Counter_input.txt","r")
for line in file_txt:
	co.update(line.lower())
print co