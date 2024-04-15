def count_words(input_str):
    word_count = 0
    inside_word = False

    for char in input_str:
        if char != ' ' and not inside_word:
            word_count += 1
            inside_word = True
        elif char == ' ':
            inside_word = False

    return word_count

user_input = input("Введите строку: ")
word_count = count_words(user_input)
print("Количество слов в строке:", word_count)
