def replace_middle_h(input_str):
    first_h_index = input_str.find('h')  # Находим индекс первого вхождения буквы 'h'
    last_h_index = input_str.rfind('h')  # Находим индекс последнего вхождения буквы 'h'

    if first_h_index != -1 and last_h_index != -1:  # Проверяем, что оба вхождения найдены
        # Заменяем все вхождения буквы 'h' на 'H', кроме первого и последнего
        replaced_str = input_str[:first_h_index + 1] + input_str[first_h_index + 1:last_h_index].replace('h', 'H') + input_str[last_h_index:]
        return replaced_str
    else:
        return input_str  # Если нет вхождений 'h', возвращаем исходную строку

# Пример использования:
user_input = input("Введите строку: ")
result = replace_middle_h(user_input)
print("Результат замены:", result)
