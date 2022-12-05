is_finish = False


def get_points():
    year10 = int(input('כמה נקודות קיבלה שכבת י: '))
    year11 = int(input('כמה נקודות קיבלה שכבת יא: '))
    return year10, year11


while not is_finish:
    year10, year11 = get_points()
    if year10 == year11:
        print("Error pls input the right amount of points each year got")
        get_points()
    if year10 > year11:
        print(year10)
        print(year10 - year11)
        is_finish = True
    else:
        print(year11)
        print(year11 - year10)
        is_finish = True
