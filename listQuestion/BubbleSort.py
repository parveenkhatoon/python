

# a=[2,75,3,4,4,56,34]
# index=0
# while index<len(a)-1:
#     if a[index]>a[index+1]:
#         b=a[index]
#         a[index]=a[index+1]
#         a[index+1]=b
#     index+=1
# print(a)




a=[3,-23,6,-2,232,56]
index=0
while index<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    index+=1
print(a)

















