#pattern
'''*
   * *
   * * *
   * * * *
   * * * * * '''

num=5
i=0
while i<num:
    j=4
    while j>=1:
        print(end=" ")
        j-=1
    n=i
    while n>0:
        print("*",end=" ")
        n-=1
    print()
    i+=1