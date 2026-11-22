# Задание 10.
# Дан целочисленный массив размера N,
# содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов
# и вывести эти номера в порядке возрастания.

N = int(input("Введите N: "))

A = list(map(int, input("Введите элементы массива: ").split()))

first = 0
second = 0

for i in range(N):
    for j in range(i + 1, N):
        if A[i] == A[j]:
            first = i + 1
            second = j + 1
            break
    if first != 0:
        break

print("Номера одинаковых элементов:", first, second)