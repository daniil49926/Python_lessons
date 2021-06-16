def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def choice_prime(obj):
    return [val for i, val in enumerate(obj) if is_prime(i)]


def main():
    obj = ["a", "b", "c", "d", "e", "f", "g"]        # Тут любой итерируемый объект
    print(list(choice_prime(obj)))


main()

# зачёт! 🚀
