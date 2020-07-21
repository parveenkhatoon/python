'''Duplicates
lists mei se duplicates nikal kar, kisi 
aur list mei daal kar print karne hai.'''

list1 = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
index=0
my_list=[]
while index<len(list1):
	if list1[index] not in my_list:
		my_list.append(list1[index])
	index+=1
print(my_list)

