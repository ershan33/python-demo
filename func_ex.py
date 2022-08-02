"""
文件:   func_ex.py
作者:   二山
邮箱:   ershan_coding@outlook.com
描述:   函数
          - 函数的【定义】 -> def
          - 函数的【参数】 -> ()
            - 函数的位置参数
            - 函数的关键字参数
            - *args
            - **kwargs
            - 参数的顺序
          - 函数的【主体】 -> : 下面的内容
          - 函数的【返回值】 -> return
"""


# 螺丝刀 GIFLENS-https://media0.giphy.com/media/31us5JIjYaPzm5T3tK/200.gif
# 上螺丝 GIFLENS-https://media2.giphy.com/media/Ah5v8MUanyVDlgSSA2/200.gif
# 有一个工具 -> 使用工具
# 先有一个函数 -> 使用函数


# 函数的定义
# def -> 定义函数的关键字
# func_name -> 合法的变量命名的全部要求
# () -> 函数参数
# : -> 隔离一个代码块
def func_name():
    # -> 函数体
    # 属于当前的函数
    pass


# 定义了一个函数 -> 制作了一个工具
def tool():
    print("使用工具。")


# 调用了一个函数 -> 我们使用了一个工具
tool()

#######################################################################
# GIFLENS-https://media4.giphy.com/media/3VABWwEndM3MSgQn4h/200.gif


# 函数参数
# 1. 位置参数
def func1(name: str, age: int):
    print(f"{name} 今年 {age} 岁了。")
    print("过了一年")
    age += 1
    print(f"{name} 今年 {age} 岁了。")


func1("liiy", 3)  # 函数的调用
func1(3, "lily")
func1("lily")
#######################################################################


# 2. 关键字参数 keyword
#   键值对，键=值
def func2(name="lily", age=3):
    func1(name, age)


func2()  # 可以不写
func2(age=4)
func2(age=18, name="mike")
#######################################################################


# 3. args -> 参数列表
# sum
# * -> 解包，把一个元组拆开成不同的元素
def func3(*args):
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    print(total)


func3()
func3(1)
func3(1, 2)
func3(1, 2, 3, 4)
func3(*list(range(101)))

# print -> 参数列表
print(1, 2, 3, "a", "d", sep="-", end=";")
print()
#######################################################################


# 4. kwargs -> 关键字参数列表
def func4(**kwargs):
    # """Print a name and age.

    # :param: name, str: person name
    # :param: age, int: person age
    # """
    print(type(kwargs))
    func1(kwargs.get("name", "lily"), kwargs.get("age", 18))


# matplotlib -> 大量用到了关键字参数列表
# python -> 没有函数的重载，新的同名函数会覆盖旧的同名函数
# def func4():
#     print('nothing.')

func4(age=25)

dic = {"name": "lily", "age": 18}
dic.get("gender", "girl")
dic["age"]  # -> 取不存在的值的时候会抛出一个异常


func4(age=23)


#######################################################################


# 参数的顺序
# 1. 位置参数
# 2. 多个爱好
# *args -> 一个约定俗成
def func(name, age, *hobbies, hometown="China", **kwargs):
    print(f"{name} is {age} years old.")

    gender = kwargs.get("gender", "male")

    # if gender == "male":
    #     subject = "he"
    # else:
    #     subject = "she"

    # A?B:C
    subject = "he" if gender == "male" else "she"

    print(f"{subject} is from {hometown}")
    print(f"{subject} has hobbies: ", end=" [")
    for hobby in hobbies:
        print(hobby, end=", ")
    print(end="]\n")


func(
    "lily",  # name
    3,  # age
    "piano",
    "listen to music",
    "picture",  # -> *hobbies
    hometown="england",  # -> keyword argument
    gender="female",  # **kwargs
)

func("zhansan", 18, "xxx", "xx1", gender="male")
#######################################################################
