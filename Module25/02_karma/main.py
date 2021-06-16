import random
import logging


class KillError(BaseException):
    pass


class DrunkError(BaseException):
    pass


class CarCrashError(BaseException):
    pass


class GluttonyError(BaseException):
    pass


class DepressionError(BaseException):
    pass


class Karma:
    __max_karma = 500
    __my_karma = 0
    __err = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
    logging.basicConfig(filename="karma.log", level=logging.INFO)

    def __init__(self):
        self.point = random.randint(1, 7)

    def one_day(self):
        err = random.choice(self.__err)
        probability = random.randint(1, 10)
        try:
            if probability == 1:
                logging.info(err)
                raise err()
            self.__my_karma += self.point
        except err:
            pass

    def get_max_karma(self):
        return self.__max_karma

    def get_my_karma(self):
        return self.__my_karma


if __name__ == '__main__':
    my_karma = Karma()
    count_day = 0
    while my_karma.get_max_karma() > my_karma.get_my_karma():
        my_karma.one_day()
        count_day += 1
    print("Прошло дней {}".format(
        count_day
    ))

# зачёт! 🚀
