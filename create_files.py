import hashlib
import os
import random
import string
from collections import defaultdict
from pprint import pprint

TARGET_FOLDER = "tmp_files"


def mkdir_if_not_exists(folder_name: str) -> None:
    """如果文件夹不存在，新建一个文件夹

    Args:
        folder_name (str): 文件夹的名字
    """
    if not os.path.exists(TARGET_FOLDER):
        os.mkdir(folder_name)


def create_a_file(filename: str) -> None:
    """如果文件不存在，就新建一个文件

    Args:
        filename (str): 文件的名字
    """
    with open(filename, "w") as f:
        f.write(generate_string(1, 3, string.ascii_lowercase))


def generate_string(a: int, b: int, pool: str):
    """生成一个随机的长度为 3 到 5 的字符串

    Returns:
        str: 返回一个随机的文件名
    """
    k = random.randint(a, b)
    li = random.choices(pool, k=k)
    return "".join(li)


def generate_filename(a: int = 3, b: int = 5) -> str:
    """生成一个随机的文件名

    Returns:
        str: 返回一个随机的文件名
    """
    return generate_string(a, b, string.ascii_letters) + ".txt"


def get_cur_index(folder: str) -> int:
    """获取当前文件名的索引

    Args:
        folder (str): 目标文件夹

    Returns:
        int: 当前索引
    """
    index_li = []
    li = [f for f in os.listdir(folder) if f.endswith(".txt")]
    for file in li:
        index = os.path.splitext(file)[0]
        if index.isdigit():
            index_li.append(int(index))
    return max(index_li) + 1 if index_li else 0


def rename(folder, old_name):
    """给目录下的一个文件重命名

    Args:
        folder (str): 要重命名文件所在的目录
        old_name (str): 旧的文件名
    """
    index = get_cur_index(folder)
    old_name = os.path.join(folder, old_name)
    new_name = os.path.join(folder, f"{index}.txt")
    if old_name.endswith(".txt") and old_name != new_name:
        os.rename(old_name, new_name)


def generate_random_files():
    """生成随机的文件"""
    mkdir_if_not_exists(TARGET_FOLDER)
    for _ in range(100):
        filename = generate_filename()
        path = os.path.join(TARGET_FOLDER, filename)
        create_a_file(path)


def rename_files(folder):
    """重命名目录下的文件

    Args:
        folder (str): 目标文件夹
    """
    for file in os.listdir(folder):
        rename(folder, file)


def get_md5(file: str):
    """获取一个文件的哈希值（md5）

    Args:
        file (str): _description_

    Returns:
        _type_: _description_
    """
    if os.path.isfile(file):
        with open(file, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()


if __name__ == "__main__":
    generate_random_files()
    rename_files("tmp_files")

    files = [os.path.join(TARGET_FOLDER, x) for x in os.listdir(TARGET_FOLDER)]

    d = defaultdict(list)
    for file in files:
        if os.path.exists(file):
            d[get_md5(file)].append(file)

    duplicated = [x for x in d.items() if len(x[-1]) > 1]
    pprint(duplicated)
