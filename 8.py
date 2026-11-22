# Задание 8.
# Дан массив A размера N.
# Найти минимальный элемент из его элементов
# с четными номерами: A2, A4, A6, ...

N = int(input("Введите N: "))

A = list(map(int, input("Введите элементы массива: ").split()))

minimum = A[1]

for i in range(3, N, 2):
    if A[i] < minimum:
        minimum = A[i]

print("Минимальный элемент:", minimum)