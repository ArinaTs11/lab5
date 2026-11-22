# Задание 2.
# Дано целое число N (> 1), первый член A
# и знаменатель D геометрической прогрессии.
# Сформировать и вывести массив размера N,
# содержащий N первых членов прогрессии.

N = int(input("Введите N: "))
A = int(input("Введите A: "))
D = int(input("Введите D: "))

arr = []
element = A

for i in range(N):
    arr.append(element)
    element = element * D

print("Массив:", arr)