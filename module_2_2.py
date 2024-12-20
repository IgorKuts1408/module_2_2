
first =int(input('Введите число 1: '))
second =int(input ("Введите число 2: "))
third =int(input("Введите число 3: "))
if third==second and first:
    print('Равных чисел: 3')
elif third == second or first == second or first==third:
    print('Равных чисел: 2')
elif not third == second or first == second or first==third:
    print('Равных чисел: 0')





