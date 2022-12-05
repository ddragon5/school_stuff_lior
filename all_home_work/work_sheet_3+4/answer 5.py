name = input("name of the factory: ")
amount = int(input('how many tires does the cars have? '))
if amount >= 4:
    print(name, 'HEAVY')
if amount == 2:
    print(name, "TWO")
if amount <= 1:
    print(name, "ERROR")
print("Have a  good day")
