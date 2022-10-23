# 1.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
################################################################################
quarter = input(int("Enter number of quarter 1/2/3/4"))
if str(quarter).isdigit() != True:
     print('It is not integer')
elif quarter == 1:
    print("x = [0...inf], y = [0...inf]")
elif quarter == 2:
    print("x = [0...inf], y = [-inf...0]")
elif quarter == 3:
    print("x = [-inf...0], y = [-inf...0]")
else: print("x = [-inf...0], y = [0...inf]")