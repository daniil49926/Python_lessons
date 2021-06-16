students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def func(students_dict):
    lst = []
    string = ''
    for _, value in students_dict.items():
        lst += value['interests']
        string += value['surname']
    return lst, len(string)


pairs = []
for key, age in students.items():
    pairs.append((key, age['age']))
print(pairs)

my_lst, size_str = func(students)
print(my_lst, size_str)

# зачёт! 🚀
