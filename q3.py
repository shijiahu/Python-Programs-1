# 3. Time_sample[123] and time_sample -: write a regex for
# this to get both these from a file.Steps to follow will be 
# read from a file and find the two pattern mentioned in that file

import re

def multi_re_find(patterns, phrase):
	for pattern in patterns:
		print('Searching the phrase using the re check: %r' %(pattern))
		print(re.findall(pattern, phrase))
myfile = open('test.txt')
test_phrase = myfile.read()
test_patterns = ['[123]','-']

multi_re_find(test_patterns, test_phrase)
