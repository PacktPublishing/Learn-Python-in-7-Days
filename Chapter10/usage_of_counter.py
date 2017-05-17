import collections 

c = collections.Counter('King TutanKhamen was the youngest Pharoah')
print c
for letter in 'What a king?':
	print '%s : %d' % (letter, c[letter])
	