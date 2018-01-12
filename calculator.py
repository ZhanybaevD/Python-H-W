def calc(*args, operators):
	if operator == '+':
		res = 0
		for i in args:
			res += i

	if operator == '*':
		res = 1
		for i in args:
			res *= i

	if operator == '/':
		for i in range(0,len(args)):
			res = args[i-1] - args[i]

	if operator == '-':
		for i in range(0,len(args)):
			res = args[i-1] - args[i]		


	return res 


numbers = [int(n) for n in input('Enter some numbers: ').split()]
operator = input('Enter any operator: ')

print(calc(*numbers, operators=operator))