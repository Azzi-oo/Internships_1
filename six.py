def format_name(full_name):
    name_parts = full_name.split()

    surname = name_parts[0]

    initials = ''.join([word[0] + '.' for word in name_parts[1:]])

    formatted_name = f"{surname} {initials}"

    return formatted_name

user_input = input("Введите имя, отчество и фамилию человека: ")
result = format_name(user_input)
print("Результат форматирования:", result)
