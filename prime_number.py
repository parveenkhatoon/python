def primeorNot(num):     
    if num > 0:
        for i in range(2,num):
            if (num % i) == 0:
                return(num,"is not a prime number")
                return(i,"times",num//i,"is",num)
                break
            else:
                return(num,"is a prime number")

    else:
           return(num,"is not a prime number")
num=int(input("Enter the number:-"))
print(primeorNot(num))