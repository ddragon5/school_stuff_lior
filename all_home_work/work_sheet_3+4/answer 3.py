name = input('מה השם שלך? ')
absentes = int(input('כמה חיסורים קיבלת/ה? '))

print(name, end='')
if absentes >= 5:
    print(' WARNING')
if absentes == 0:
    print(' EXCELLENT')
print('אתה קיבלת/ה', absentes, 'החודש')
