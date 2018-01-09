# #1

# dic1 = {1:10, 2:20} 
# dic2 = {3:30, 4:40} 
# dic3 = {5:50,6:60}

# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)



# #2

# n = 5
# dic = {x: (x*x) for x in range(1, n+1)}
# print(dic)


# #3

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = dict()
# for i in d1:
# 	if i in d3:
# 		d3[i] += d1[i]
# 	else:
# 	    d3[i] = d1[i]
# for i in d2:
# 	if i in d3:
# 		d3[i] += d2[i]
# 	else:
# 	    d3[i] = d2[i]		    	
# print(d3)


# #4
# first = list()
# second = list()
# Complete = list()
# dic = {'1':['a','b'], '2':['c','d']}
# first = dic['1']
# second = dic['2']
# for i in first:
# 	for x in second:
# 		Complete.append(i+x)
# for i in Complete:	
# 	print(i)



#5
# sometext = 'december2017'
# diction = dict() 
# for i in sometext:
# 	if i in diction:
# 		diction[i] += 1
# 	else:
# 		diction[i] = 1


# 		print(diction)


