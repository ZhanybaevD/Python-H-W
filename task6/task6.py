#1

text = open('./chuck.txt', 'r')
data = text.read()
len_text = len(data)
str_text = str(len_text)




new_file = open('./abc.txt', 'w')
try:
	for i in str_text:
		new_file.write(i)
except Exception as e:
	print('Error: ', e)	
finally:
	new_file.close()
	print('closed')
	text.close()



print(len_text)



#2

open_chuck = open('./chuck.txt', 'a')
text2 = "Chuck Norris doesn't go hunting... CHUCK NORRIS GOES KILLING.What was going through the minds of all of Chuck Norris\' victims before they died? His shoe Fool me once, shame on you. Fool Chuck Norris once and he will roundhouse you in the face, Chuck Norris drives an ice cream truck covered in human skulls Chuck Norris doesn\'t wear a watch. HE decides what time it is, There are more Chuck Norris facts than there are galaxies in the universe. Scientists have estimated that the energy given off during the Big Bang is roughly equal to 1CNRhK (Chuck Norris Roundhouse Kick). Chuck Norris counted to infinity - twice Most people have 23 pairs of chromosomes. Chuck Norris has 72... and they\'re all poisonous, A Handicapped parking sign does not signify that this spot is for handicapped people. It is actually in fact a warning, that the spot belongs to Chuck Norris and that you will be handicapped if you park there, Outer space exists because it\'s afraid to be on the same planet with Chuck Norris A Handicapped parking sign does not signify that this spot is for handicapped people. It is actually in fact a warning, that the spot belongs to Chuck Norris and that you will be handicapped if you park there, The Great Wall of China was originally created to keep Chuck Norris out. It failed miserably, Police label anyone attacking Chuck Norris as a Code 45-11... a suicide, Police label anyone attacking Chuck Norris as a Code 45-11... a suicide.Chuck Norris doesn't read books. He stares them down until he gets the information he wants, Chuck Norris does not call the wrong number you answer the wrong number."
open_chuck.write(text2)
open_chuck.close()



with open('./chuck.txt', 'r') as f:
	data = f.read().lower()
	print(data.count('chuck norris'))
		