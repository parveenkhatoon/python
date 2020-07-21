
'''swaping with using comma'''
a=10
b=20
a,b=b,a
print(a,b)

'''swaping without using comma'''
a=10
b=20
a=a+b
b=a-b
a=a-b
print("a="a,"b=",b)


'''swaping using third '''
a=10
b=20
c=a
a=b
print("a=",c,"b=",a)