import math

#1 площадь треугольника

a = int(input('Enter value of triangle \'a\': '))
b = int(input('Enter value of triangle \'b\': '))
c = int(input('Enter value of triangle \'c\': '))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p -c))
print('S = ', s, 'cm')


#2 площадь круга 

R = int(input('Enter value of circle\'s radius : '))
S = math.pi * (R ** 2)
print('S = ', S, 'cm')

#3 площадь квадрата 
a_2 = int(input('Enter value of square: '))
s_3 = math.sqrt(a_2 ** a_2)
print(s_3)