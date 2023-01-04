from random import randint

length = 8

# Список, сгенерированный функцией randint
L = []

# Список указанный вручную
# list2 = [1, 23, 4, 86, 13, 98, 56, 3, 6, 10, 12, 20, 76, 34, 90]

for i in range(length):
    L.append(randint(0, 100))

print(L)

for i in range(length-1):
    for j in range(length-i-1):
        # наглядный вывод итераций
        # print('i=', i, 'iter: ', length-i-1, L[j] > L[j+1], L)
        if L[j] > L[j+1]:
            # Можно написать команду в одну строку
            # L[j], L[j+1] = L[j+1], L[j]
            # Можно использовать временную переменную
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp

print(L)