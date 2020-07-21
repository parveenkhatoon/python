

my_list=[500,40,23,70,12,56,5,10,7]
index=0
first_max=0
sec_max=0
while index<len(my_list):
	if first_max<my_list[index]:
		first_max=my_list[index]
	index=index+1
	index1=0
	while index1<len(my_list):
		if first_max>my_list[index1] and sec_max<my_list[index1]:
			sec_max=my_list[index1]
		index1=index1+1
print(first_max)	
print(sec_max)

