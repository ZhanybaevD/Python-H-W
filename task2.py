#Task1
a = [7, 2, 0, -6, 12, 100, 4, 36, 9, 2]
a.sort()
a.reverse()	
print(a)

#Task2

ASlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ASlist.insert( 2, -1)
ASlist.pop(6)

print(ASlist)

#Task3
text = 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using "Content here, content here", making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'
IPtext = text.split() 
PredText = text.split('.')
lenText = len(IPtext)
lenPredText = len(PredText)
s = '.'
print(IPtext)
print('Words:', lenText)
print('Stans:', lenPredText)
print(s.join(PredText[-3:]))
