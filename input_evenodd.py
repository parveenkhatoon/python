def showNumber():
    num=int(input("Enter the number:"))
    i=0
    while i<=num:
        if i%2==0:
            print(i,"Even")
        else:
            print(i,"Odd")
        i+=1
showNumber()
