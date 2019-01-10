# 8. Write a program to remove duplicate and return the length of
# the unique list (eg a = [1,1,3,4] will return a = [1,3,4] and the length will be 3)
def removeDup(nums):
	# print(list(set(nums)), len(list(set(nums))))
	unique = []
	for x in nums:
		if x not in unique:
			unique.append(x)
	print(unique, len(unique))

removeDup([1,1,3,4])