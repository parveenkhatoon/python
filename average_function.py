def average_and_sum():
    i=1
    sum=0
    average=0
    while i<=3:
        num=int(input("Enter first number:"))
        sum=sum+num
        average=sum/i
        i+=1
    print("sum of three number:-",sum)
    print("average of three number:-",average)
average_and_sum()

