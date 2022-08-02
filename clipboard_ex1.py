import clipboard

text = clipboard.paste()
output = text.title()
clipboard.copy(output)


def to_title():
    """-> docstring，文档字符串

    1. 从剪贴板获取文本数据
    2. 将文本数据更改为标题形式
    3. 把处理过的文本放到剪贴板里面
    """
    text = clipboard.paste()
    output = text.title()
    clipboard.copy(output)


print(f"{__file__}: {__name__}")


# 程序的入口
if __name__ == "__main__":
    to_title()
    print("from main")
