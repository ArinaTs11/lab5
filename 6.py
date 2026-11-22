# Задание 6.
# Дан массив размера N и целые числа K и L
# (1 <= K <= L <= N).
# Найти среднее арифметическое элементов массива
# с номерами от K до L включительно.

N = int(input("Введите N: "))

A = list(map(int, input("Введите элементы массива: ").split()))

K = int(input("Введите K: "))
L = int(input("Введите L: "))

total = 0

for i in range(K - 1, L):
    total += A[i]

average = total / (L - K + 1)

print("Среднее арифметическое:", average)