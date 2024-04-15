array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]

# Транспонирование списка с помощью спискового включения
transposed_array = [[row[i] for row in array] for i in range(len(array[0]))]

# Вывод результата транспонирования
for row in transposed_array:
    print(row)
