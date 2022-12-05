amount = int(input('כמה מנות הזמנת/ה: '))
price = int(input('כמה עלתה כל מנה שהזמנת/ה: '))
if amount >= 50:
    amount = amount - 2
total_price = amount * price
print(total_price)
