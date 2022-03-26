from functools import reduce


import clipboard


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
    
    面向过程的编程
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
    # pipeline(str.lower)  # 我们传了一个函数作为程序参数 1, 2, 3 mike
    # pipeline(lambda x: "".join([c for c in x if c.isascii() or c == " "]))


if __name__ == "__main__":
    main()
