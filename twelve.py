
a = input("Введите числа, разделенные запятой: ")

b = a.split(',')

# Преобразуем каждую строку в число и создаем список чисел
b = [int(num) for num in b]

numbers_tuple = tuple(b)

print("Список чисел:", b)
print("Кортеж чисел:", numbers_tuple)
