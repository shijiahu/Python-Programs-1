# 10. Write a program that accepts a sentence and 
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def func_find(s):
	count_upper, count_lower = 0, 0
	for x in s:
		if x.isupper():
			count_upper += 1
		elif x.islower():
			count_lower += 1
	print('UPPER CASE ' + str(count_upper))
	print('LOWER CASE ' + str(count_lower))

func_find('Hello world!')