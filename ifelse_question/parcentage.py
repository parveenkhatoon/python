x = int(input("Enter held cless:"))
y = int(input("Enter attended_clesses:"))
percentage_clesses=(100/x*y)
if percentage_clesses >= 75:
    print("allowed to sit an exam",percentage_clesses)
else:
    print("no sit an exam")
