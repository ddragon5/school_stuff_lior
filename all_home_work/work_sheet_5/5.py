num = input("input a dubel or triple digit number: ")
digits = []
for c in num:
    digits.append(int(c))

if len(digits) == 2:
    finaly_num = digits[1] * 10
    finaly_num = finaly_num + digits[0]
    finaly_num = finaly_num + 1

if len(digits) == 3:
    finaly_num = digits[2] * 100
    finaly_num = finaly_num + digits[1] * 10
    finaly_num = finaly_num + digits[0] + 1

print(finaly_num)
