# filter

numbers = [1,2,3,4,5,6,7,8,9,10]

lil = list()

def filter_func():
	for i in numbers:
		if 2 <= i <=7:
			lil.append(i)
	return lil


print(filter_func())

# reduce 
from functools import reduce

array = [1,2,3,4,5]

def reduce_func():
	res = 1
	for i in array:
		res *= i
	return res

print(reduce_func())
print(reduce(lambda x, y: x * y, [1,2,3,4,5,6]))		

