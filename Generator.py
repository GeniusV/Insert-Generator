#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

# Created By GeniusV at 201707292333


class Factory:
    def get(self):
        pass


class DateGenerator:
    __tb_name = ''
    isinstance(__tb_name, str)
    __field = {}
    isinstance(__field, dict)
    __num = 0

    def __init__(self, table_name, field, num):
        self.__tb_name = table_name
        self.__field = field
        self.__num = num

    def __convert(self):
        field_name = []
        field_value = []
        for i in self.__field:
            field_name.append(i)
            if isinstance(self.__field[i], Factory):
                field_value.append(self.__field[i].get())
            else:
                field_value.append(self.__field[i])
            if isinstance(field_value[-1], str):
                field_value[-1] = "'" + field_value[-1] + "'"
            else:
                field_value[-1] = str(field_value[-1])
        return field_name, field_value

    def run(self):
        for i in range(self.__num):
            common = ', '
            field_name, field_value = self.__convert()
            print("INSERT INTO {} ({}) VALUES ({});".format(self.__tb_name, common.join(field_name),
                                                            common.join(field_value)))

