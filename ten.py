def are_all_unique(seq):
    return len(set(seq)) == len(seq)

# Пример использования функции
sequence1 = [1, 2, 3, 4, 5]
# sequence2 = [1, 2, 3, 4, 4]

print("Все числа в sequence1 уникальны?", are_all_unique(sequence1))
