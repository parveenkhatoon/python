
student_marks = [50, 40, 23, 70, 56, 12, 5, 10, 7]
index = 0
less_than40 = 0
more_than20 = 0
while index < len(student_marks):
    marks = student_marks[index]
    if marks < 40:
        less_than40 = less_than40 + 1
    else:
        more_than20 = more_than20 + 1
    index = index + 1
print ("number more than 20: ",(more_than20))
print ("number less than 40: ",(less_than40))
