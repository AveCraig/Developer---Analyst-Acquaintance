# 2.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
################################################################################
a = input("Enter coordinates for point A, use a space separator:")
b = input("Enter coordinates for point B, use a space separator:")
a = a.split()
b = b.split()
a_x = float(a[0])
a_y = float(a[1])
b_x = float(b[0])
b_y = float(b[1])

d = ((b_x - a_x) ** 2 + (b_y - a_y) ** 2) ** 0.5

print(d)