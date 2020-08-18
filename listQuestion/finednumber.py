
'''Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,6,7 
find which numbers are not present in the second array.'''

list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
index=0
list3=[]
while index<len(list1):
    if list1[index]  not in list2:
        list3.append(list1[index])
    index=index+1
print(list3)
