# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
################################################################################
day_of_the_week = int(input("Enter the day of the week in numerical format :"))
if str(day_of_the_week).isdigit() != True:
    print('It is not integer')
elif day_of_the_week < 1 or day_of_the_week > 8:
    print('Please use numbers 1/2/3/4/5/6/7')
elif day_of_the_week < 6:
    print("Go to work")
elif day_of_the_week > 5:
    print("Time to relax")
else:print('Well done')