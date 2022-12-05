name = input('what is your name? ')
classes = int(input('לכמה חוגים נרשמת/ה? '))
price = 100
total_price = classes * price

print(name, 'אתה צריך לשלם', total_price, 'שקלים')
if classes >= 5:
    print(name, "GIFT")
