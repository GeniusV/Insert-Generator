import random

from Generator import Factory


class PhoneNumFactory(Factory):
    __head = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 187, 188,
              130, 131, 132, 155, 156, 185, 186,
              133, 153, 180, 189]

    def get(self):
        list = []
        for i in range(8):
            list.append(str(random.randint(0, 9)))
        return str(random.choice(self.__head)) + str(''.join(list))