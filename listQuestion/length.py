'''finding a length without using length function in 
for loop'''

my_list=[50,40,23,70,56,12,5,10,7]
print(my_list)
count=0
for i in my_list:
	count+=1
print(count) 



'''finding a length without using length function in 
while loop'''

my_list=[50,40,23,70,56,12,5,10,7]
print(my_list)
count=0
while my_list[count:]:
    count+=1
print(count)





