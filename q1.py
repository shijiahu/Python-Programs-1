# 1. Write a function to generate Fibinocci series
def fun(x):
	def fib(x):
		if x == 0:
			return 0
		elif x == 1:
			return 1
		else:
			return fib(x - 1) + fib(x - 2)

	for i in range(6):
		print(fib(i))

# test
fun(6)