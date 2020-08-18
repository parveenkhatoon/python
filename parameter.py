def parameter_multiples():
    num=int(input("Enter the number:"))
    i=0
    sum=0
    while i<=num:
        if i%5==0 or i%3==0:
            sum=sum+i
        i+=1
    print(sum)
parameter_multiples()


