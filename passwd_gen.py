"""
0. 智能提示
1. 自动补全
2. 自动导入
3. 运行选择的区域
    - shift + enter
    - 选中区域后点击右键 run selection
4. 运行整个文件
    - 点击右上角的小三角
    - 打开命令面板搜索 python: run
    - 点击右键选择 run python file in terminal
"""


import random
import string


def gen_password(count=10):
    alpha = string.ascii_letters
    number = string.digits
    li = []
    for _ in range(count):
        char = random.choice(alpha + number)
        li.append(char)

    return "".join(li)


passwd = gen_password(18)
print(passwd)
