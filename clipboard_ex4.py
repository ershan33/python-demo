import tkinter as tk  # python 标准库提供的图形化界面

import clipboard

"""
图形化界面：对交互式要求比较强
    - office
    - adobe
命令行界面: 常用于服务器端
    - linux/unix
"""


def to_title():
    """
    1. 从剪贴板获取文本数据
    2. 将文本数据更改为标题形式
    3. 把处理过的文本放到剪贴板里面
    """
    text = clipboard.paste()
    output = text.title()
    clipboard.copy(output)


def merge_lines():
    """
    1. 从剪贴板获取文本数据
    2. 将文本数据里的 \r\n or \n 给替换掉
    3. 把处理过的文本放到剪贴板里面
    """
    text = clipboard.paste()
    end = "\r\n" if "\r\n" in text else "\n"
    output = text.replace(end, "")
    clipboard.copy(output)


def pipeline(process=lambda x: x):
    """
    1. 从剪贴板获取文本数据
    2. 处理文本数据
    3. 把处理过的文本放到剪贴板里面
    """
    text = clipboard.paste()
    output = process(text)
    clipboard.copy(output)


def ml(text: str):
    """Merge Lines"""
    end = "\r\n" if "\r\n" in text else "\n"
    output = text.replace(end, "")
    return output


def main():
    pipeline(ml)


if __name__ == "__main__":
    # 图形化界面的一个解决方式
    # 列表 list -> 最常用的容器数据结构
    # 定义非常简单，[]
    text_li = ["to title", "merge lines"]
    func_li = [to_title, merge_lines]

    window = tk.Tk()
    # [exp for each in li] exp -> 最终元素的形态
    # [tk.Button(), tk.Button(), ...]
    # buttons_copy = []
    # for text, func in zip(text_li, func_li):
    #     buttons_copy.append(tk.Button(text=text, command=func))
    buttons = [tk.Button(text=t, command=f) for t, f in zip(text_li, func_li)]

    # for but in buttons:
    #     but.pack()
    ret = [but.pack() for but in buttons]  # -> [None, None]
    print(ret)

    exit_but = tk.Button(text="exit", command=window.destroy)
    exit_but.pack()
    window.mainloop()
