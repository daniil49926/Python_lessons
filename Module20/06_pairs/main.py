num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first_list = [i for i in num_list if num_list.index(i) % 2 == 0]
second_list = [i for i in num_list if num_list.index(i) % 2 != 0]
print(list(zip(first_list, second_list)))

# зачёт! 🚀
