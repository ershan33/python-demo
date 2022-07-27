# 使用 Python 调用 C 代码

## 指南

1. 编译 c 代码为动态链接库

```sh
gcc -c -Wall -Werror -fpic sample.c
gcc -shared -o libsample.so sample.o
```

2. 使用 python 调用动态链接库

```python
>>> import sample
>>> sample.gcd(35,42)
7
>>> sample.in_mandel(0,0,500)
1
>>> sample.in_mandel(2.0,1.0,500)
0
>>> sample.divide(42,8)
(5, 2)
>>> sample.avg([1,2,3])
2.0
>>> p1 = sample.Point(1,2)
>>> p2 = sample.Point(4,5)
>>> sample.distance(p1,p2)
4.242640687119285
```




## 引用

1. [Python Cookbook](https://github.com/dabeaz/python-cookbook) -- chapater 15
2. [Shared libraries with GCC on Linux](https://www.cprogramming.com/tutorial/shared-libraries-linux-gcc.html)