# 7. Write a program to find the number of 'a' followed by 0 in a string(eg a0kkka0hdhda0 should return the count 3)

import re

def num_zero(s):
	mylist = re.findall('a0', s)
	# print(mylist)
	return len(mylist)


print(num_zero('a0kkka0hdhda0'))

