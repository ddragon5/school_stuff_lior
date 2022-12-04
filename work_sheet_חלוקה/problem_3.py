# getting the number of students
num_of_students = int(input("please input the number of students: "))
# calc of the number capsules
num_of_capsules = num_of_students / 20
# checking if num_of_capsules is not a decimal number
if type(num_of_capsules) == float:
    # if it then round down and add another capsule
    num_of_capsules = num_of_students // 20
    num_of_capsules = num_of_capsules + 1

print("the number of capsules needed is ", end='')
print(num_of_capsules)
