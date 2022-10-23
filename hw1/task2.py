# 1.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
################################################################################
x = input("Enter X: ")
y = input("Enter Y: ")
z = input("Enter Z: ")

check_equal = (not (x or y or z)) == (not x and not y and not z)

if check_equal == True:
    print(f"The statement is true")
else:
    print(f"The statement is false")
