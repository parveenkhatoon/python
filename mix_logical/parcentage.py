medical_couse=input("enter the couse:yes/no:")
classheld=int(input("enter cless of held:"))
attendence=int(input("enter the attenedce:"))
parcentage=(attendence/classheld*100)
if medical_couse =="no":
    if parcentage>=75:
        print("allowed to sit axem",parcentage)
    else:
        print("not allowed to sit")
else:
    print("you can sit")