age = int(input("what is your age: "))
amount = int(input("how many tickets do you want to buy? "))
if age <= 18:
    total_price = amount * 40
    print("YOUTH")
else:
    total_price = amount * 60
    print("ADULT")
print(total_price)
