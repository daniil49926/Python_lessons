class Stack:
    def __init__(self):
        self.__my_stack = []
        self.__nums_task = 0

    def push(self, obj):
        self.__my_stack.append(obj)
        print("{} - добавлен в стек".format(str(obj)))

    def pop(self):
        obj = self.__my_stack.pop()
        print("{} - удален".format(obj))

    def sort(self):
        return self.__my_stack.sort(key=lambda x: x[0])  # для сортировки только по приоритету(первому знаку)

    def get_obj(self):
        return self.__my_stack


class TaskManager:
    def __init__(self):
        self.__task_stack = Stack()

    def new_task(self, task, priority):
        __my_task = "{} {}".format(
            priority, task
        )
        self.__task_stack.push(__my_task)
        self.__task_stack.sort()

    def __call__(self):
        ret_str = str(self.__task_stack.get_obj())
        return ret_str[1:-1]


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("сдать дз", 2)
manager.new_task("поесть", 2)

print(manager())

# зачёт! 🚀
