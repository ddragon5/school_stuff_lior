name = input('what is your name? ')
drove = int(input('כמה קטעים עברת? '))
price = 30
total_price = drove * price

if drove >= 8:
    total_price = total_price - 10
print(name, 'אתה צריך לשלם', total_price, 'שקלים')
