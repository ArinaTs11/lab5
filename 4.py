# Задание 4.
# Дан массив A размера N.
# Вывести его элементы в следующем порядке:
# A1, AN, A2, AN-1, A3, AN-2, ...

N = int(input("Введите N: "))

A = list(map(int, input("Введите элементы массива: ").split()))

for i in range(N // 2):
    print(A[i], A[N - 1 - i], end=" ")

if N % 2 == 1:
    print(A[N // 2], end=" ")