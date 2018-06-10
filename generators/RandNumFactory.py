#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/10/18.
import random

from Generator import Factory


class RandNumFactory(Factory):
    def __init__(self, start = 0, end = 100):
        self.__start = start
        self.__end  = end

    def get(self):
        return random.randint(self.__start, self.__end)
