"""
文件:   thread_ex.py
作者:   二山
邮箱:   ershan_coding@outlook.com
描述:   Python 多线程的例子
"""


import threading
import time

import clipboard

Flag = True


def backend():
    global Flag
    while Flag:
        text = clipboard.paste()
        clipboard.copy(text.upper())
        time.sleep(0.01)
    print("exit")


if __name__ == "__main__":
    th = threading.Thread(target=backend)
    th.start()

    while True:
        flag = input(">>> ")
        if flag.casefold() == "q":
            Flag = False
            break
        elif flag.casefold() == "print":
            print("from main")
        else:
            print("unknown command")
