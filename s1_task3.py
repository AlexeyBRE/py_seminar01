'''Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
 точек в этой четверти (x и y).
1 -> x > 0, y > 0'''
quarter = int(input("Введите четверть: "))
if quarter == 1:
    print(f"{quarter} -> x > 0, y > 0")
elif quarter == 2:
    print(f"{quarter} -> x < 0, y > 0 ")
elif quarter == 3:
    print(f"{quarter} -> x < 0, y < 0")
elif quarter == 4:
    print(f"{quarter} -> x > 0, y < 0")
else:
    print("Такого номера четверти не существует")