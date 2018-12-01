# -*-coding:utf-8 -*-
# File :property_test.py
# Author:George
# Date : 2018/11/26

class Student(object):

    def __init__(self, name, age, score=75):
        """

        :param name:
        :param age:
        :param score:
        """
        self.name = name
        self._age = age
        self.score = score

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def get_age(self, age):
        if not isinstance(age, int):
            raise ValueError('Invalid age!')
        if age < 0 or age > 120:
            raise ValueError('Illogical input')
        self._age = age

    @get_age.deleter
    def get_age(self):
        del self._age


if __name__ == "__main__":
    george = Student('george', 32, 96)
    # 这样才是正常调用get_age的正确姿势
    george.get_age = -23
    print(george.get_age)
