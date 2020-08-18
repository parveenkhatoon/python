def sumofdigits(number):
    sum=0
    while number!=0 :
        modulus=number%10
        sum+=modulus
        number/=10
    return sum
number=int(input("Enter the number:"))
print(sumofdigits(number))