import random

from Generator import Factory


class PasswordFactory(Factory):
    __list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
              'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
              'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    __digit = 0

    def __init__(self, digit = 8):
        super().__init__()
        self.__digit = digit

    def get(self):
        ls = []
        for i in range(self.__digit):
            ls.append(str(random.choice(self.__list)))

        return str(''.join(ls))

