students = int(input('how many tickets wore ordered: '))
if students <= 100:
    price = 48
else:
    price = 43
total_price = students * price
print("the price is ", total_price, 'shekels')
