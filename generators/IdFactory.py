#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# Created by GeniusV on 6/10/18.
from Generator import Factory


class IdFactory(Factory):
    __ct = 0

    def __init__(self, start = 1):
        self.__ct = start - 1


    def get(self):
        self.__ct += 1
        return self.__ct
