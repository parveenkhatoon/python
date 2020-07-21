'''Total Sum
Q: How to find
 all pairs in an array of integers whose sum is 
 equal to the given number?'''

number=30
n = [10, 11, 12, 13, 14, 17, 18, 19]
index=0
my_list=[]
while index<len(n):
    j=index-1
    sum1=0
    while j<len(n):
        sum1=n[j]+n[index]
        if sum1==number:
            a=[n[j],n[index]]
            my_list.append(a)
        j=j+1
    index=index+1
print(my_list)

















