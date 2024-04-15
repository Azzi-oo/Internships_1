# Исходные списки
list1 = [3, 1, 4, 2]
list2 = [5, 6, 2, 1]

combined_list = list1 + list2
combined_list.sort()

unique_sorted_list = list(set(combined_list))

print("Отсортированный список без повторов:", unique_sorted_list)
