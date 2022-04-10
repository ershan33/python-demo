'''
文件:   oop_ex.py
作者:   二山
邮箱:   ershan_coding@outlook.com
描述:   类，对象，实例，实例属性和方法，
        类属性和方法，静态方法  
'''


# Python 一切皆对象

# Python 对象 （objct）
# - 内存地址
# - 类型
# - 值

# id(3)
# type(3)
# 3  # 字面量
# 
# s = 's'
# id(s)
# type(s)
# s  # 变量
# 
# id(print)
# type(print)
# print


# class -> 类型，种类 （对象） -> 人类
class Person:
    # 类也有属性
    total_cnt = 0
    total_age = 0

    # 构造函数
    def __init__(self, name, age, gender) -> None:
        # 实例的属性
        self.name = name
        self.age = age
        self.gender = gender
        Person.total_cnt += 1
        Person.total_age += age

    # 实例方法
    def say_hi(self):
        print(self.name, 'hi')

    @classmethod
    def average_age(cls):
        return Person.total_age / Person.total_cnt

    # 静态方法
    # 这个方法既没有使用类的属性和方法
    # 也没有使用实例的属性和方法
    @staticmethod
    def func():
        print("this is a function")


if __name__ == "__main__":
    # Person, int, str -> p1，3，'python'
    p1 = Person("p1", 18, 'male')  # 实例化：通过类型(Person)
                                   # 创建实例(p1)的过程
    id(p1)
    type(p1)
    p1

    mike = Person('mike', 18, 'male')
    lily = Person('lily', 15, 'female')
    Person.total_cnt
    Person.total_age
    Person.average_age()
    mike.say_hi()

    Person.say_hi(mike)
    mike.func()
    Person.func()