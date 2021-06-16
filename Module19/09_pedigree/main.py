def height(human):
    if human not in tree:
        return 0
    else:
        return 1 + height(tree[human])


tree = {}
num_of_human = int(input("Введите кол-во пар людей: "))
for i in range(num_of_human):
    child, parent = input("{num} пара - ".format(
        num=(i + 1)
    )).split()
    tree[child] = parent

heights = {}
for i in set(tree.keys()).union(set(tree.values())):
    heights[i] = height(i)

for key, value in sorted(heights.items()):
    print(key, "\t", value)
