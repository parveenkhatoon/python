
'''we have one list in that list if we found nagitive 
number than number reples to 0'''

list1=[2,-3,1,6,4,-5,-3,4]
index=0
lenght = len(list1)
while index<lenght:
	if list1[index]<0:
		list1.remove(list1[index])
		list1.insert(list1[index],0)
	index+=1
print(list1)
