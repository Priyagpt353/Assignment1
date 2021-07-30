
#Ques1- Delete all occurrences of an element in a list
mylist = [1,2,3,4,5,4,7,6]
repeat = 4

#remove the item for all its occurrences
for item in mylist:
	if(item==repeat):
		mylist.remove(repeat)

print(mylist)

