def zip2(obj1, obj2, count=0):
    try:
        print((obj1[count], obj2[count]), end=" ")
        return zip2(obj1, obj2, count=count+1)
    except IndexError:                          # Не нашел другого способа остановить рекурсию не используя
        return 0                                # циклы и условия


my_list = [1, 2, 3, 4]
my_str = "Python"
zip2(my_list, my_str)

# зачёт! 🚀
