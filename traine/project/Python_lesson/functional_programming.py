def my_filter(num):
    if num % 2 == 0:
        return num


def adder(num):
    return num + 2


my_num = [1, 2, 3, 4, 5, 6, 7, 8]
result = map(adder, filter(my_filter, my_num))  # применяем функцию adder ко всем числам которые вернет фильтр
print(list(result))
nums_result = sum(map(adder, filter(my_filter, my_num)))
print(nums_result)


my_num = [1, 2, 3, 4, 5, 6, 7, 8]
result = map(lambda x: x + 10, my_num)
print(list(result))


my_numbers = [1, 3, 4, 10, 9]
result = [x * 3 for x in my_numbers if x % 2]  # создаем лист с условием
print(result)

my_numbers1 = [1, 3, 4, 10, 9]
my_numbers2 = [2, 5, 8, 7]
result = [x * y for x in my_numbers1 for y in my_numbers2 if x % 2 and y // 2]  # создаем лист из двух с условием
print(result)

my_numbers = [1, 3, 4, 10, 9]
result = {x for x in my_numbers}  # создаем множество(set) с условием
print(result)

my_numbers = [1, 3, 4, 10, 9]
result = {x: x ** 2 for x in my_numbers if x % 2}  # создаем словарь с условием
print(result)