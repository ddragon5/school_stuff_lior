num = int(input("enter a number: "))

check = num / 7 - num // 7
if check == 0:
    Boom = True
else:
    Boom = False

if Boom == False:
    print(num)
else:
    print("boom".upper())
