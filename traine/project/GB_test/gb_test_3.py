число=input("Число: ")  # Крайне не рекомендуется называть переменный символами Кириллицы,
# используйте Кириллицу только для комментариев
i  =int(число)  # Постарайтесь избегать использование имен с одним символом,
ii =int(число+число)  # а также старайтесь называть переменные осмысленно
iii=int(число+число+число)
sum = i+ii+iii  # Не стоить заводить переменную с названием sum, т.к. это встроенная функция Python,
print(sum)  # при создание переменной с таким именем вы теряете доступ к самой функции sum

# Также отделяйте операторы ( = , + , и т.п.) одним пробелом с двух сторон

# Такому ученику следует посоветовать изучить PEP8
