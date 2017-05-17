import collections

co = collections.Counter()
file_txt = open("Counter_input.txt","r")
for line in file_txt:
	co.update(line.lower())

print "Most common:\n"
for letter, count in co.most_common(5):
	print '%s: %7d' % (letter, count)