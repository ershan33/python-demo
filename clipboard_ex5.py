import time

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
    s = clipboard.paste()
    # 写一个 while 循环
    # 写一个死循环
    while True:
        try:
            if s == clipboard.paste():
                time.sleep(0.5)
            else:
                pipeline(ml)
                # update s
                s = clipboard.paste()
        except KeyboardInterrupt:
            print("exit")
            break


if __name__ == "__main__":
    # 命令行的解决方式
    main()