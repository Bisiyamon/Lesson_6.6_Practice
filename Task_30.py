""" Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """


a1 = int(input("Введите первый элемент последовательности: "))
d = int(input("Введите разность для арифметической последовательности: "))
n = int(input("Введите количество элементов: "))

array_progress = []
for i in range(n):
    array_progress.append(a1 + (i)*d)

print(array_progress)

