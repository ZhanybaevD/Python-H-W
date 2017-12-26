# First
a = [1,2,3,4,5,6,7,8,9]
print(a)
sum = 0
for i in a:
	sum = sum + i
print(sum)


#Second
b = [11,22,33,44,55,66,77]
c = b[1]
d = b[1]
for i in b:
	if c >= i:
		c = i
	if d <= i:
	   d = i
print('min', c)
print('max', d)	   	
	   	

#Third

es = [x for x in range(100) if x % 3 == 0]
print(es)