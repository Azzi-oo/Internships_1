def swap_words(input_str):
    words = input_str.split()

    words[0], words[1] = words[1], words[0]

    swapped_str = ' '.join(words)

    return swapped_str

user_input = input("Введите строку из двух слов, разделенных пробелом: ")
result = swap_words(user_input)
print("Результат после перестановки слов:", result)
