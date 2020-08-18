
binary_list=[1,1,0,0,1]
b=0
index=len(binary_list)-1
sum=0
while index>=0:
    solve=binary_list[index]*(2**b)
    sum=sum+solve
    b=b+1
    index=index-1
print sum