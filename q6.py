# 6. Check if a string is composed of all unique characters.
# eg func_unique("ajdkw") -- True func_unique("hi how are you") -- False
def func_unique(s):
	mylist = list(s)
	myset = set(mylist)
	return len(mylist) == len(myset)


print(func_unique("ajdkw"))
print(func_unique("hi how are you"))
