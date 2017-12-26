# First 
for i in range(1500, 2700):
	if (i%7==0) and (i%5==0):
		print (i)


# Second
z = 0
while z<5:
	print("*"*z)
	z+=1
	if z==5:
		while z>0:
			print("*"*z)
			z-=1
			if z==0:
				break
		break

...
