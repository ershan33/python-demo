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
    # 1. 把剪贴板里的内容粘贴到 text 这个变量里
    text = clipboard.paste()
    # 2. 识别出 text 里面的换行符
    #       win: \r\n
    #       linux: \n
    #   三元操作符 a?b:c
    #   A if B else C -> 如果 B 为 True -> A 否则 -> C
    #   str.repace
    end = "\r\n" if "\r\n" in text else "\n"
    output = text.replace(end, "")
    clipboard.copy(output)


if __name__ == "__main__":
    # to_title()
    merge_lines()
