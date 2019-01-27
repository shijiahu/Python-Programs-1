# 2. Implement Bubble sort in an optimised way to sort a million of items
l1 = [6, 3, 2, -4, -100, 0, 68, 1, 66, 100, 51, 0, 489, -4564, 64]

# with optimize flag
# not sure if this one is the best solution
def bubbleSort(nums):
	count_swap = 0
	count = 0

	if not len(nums):
		return
	for i in range(len(nums)):
		flag = False
		count += 1
		for j in range(len(nums) - i - 1):
			if nums[j] > nums[j + 1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				count_swap += 1
				flag = True
		if not flag:
			break
		# print(nums)
	# print(count, count_swap)

# test
bubbleSort(l1)
print(l1)


