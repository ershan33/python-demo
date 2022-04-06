#!/usr/bin/env python
# coding: utf-8

# # 装饰器
# 
# 函数是一等公民（first-class）
# 
# 1. 可以在函数里面定义函数（嵌套定义）
# 2. 把函数当作参数
# 3. 把函数当作返回值

# ## 函数里面定义函数

# In[1]:


def outer():
    def inner():
        '''Define an inner in outer.
        '''
        print('inner function')
    
    inner()


# In[2]:


outer()


# ## 函数作为参数

# In[3]:


def say_hi():
    print('hi')


# In[4]:


def do(method):
    print("start function")
    method()
    print("end function")


# In[5]:


do(say_hi)


# ## 函数作为返回值

# In[6]:


def add_(val):
    def add(x):
        return x + val
    
    return add


# In[7]:


add1 = add_(val=1)


# In[8]:


add1(x=1)


# In[9]:


add1(x=2)


# In[10]:


add2 = add_(2)


# In[11]:


add2(1)


# ## 装饰器
# 
# ### 装饰器的原理

# In[12]:


def print_info(func):  # 函数当作参数
    """在不改变函数定义的情况下，改变函数的行为
    """
    
    # 在函数内部定义函数
    def wrapper():
        print(f"start function {func.__name__}")
        func()
        print(f"end function {func.__name__}")
        
    return wrapper  # 函数作为返回值


# In[13]:


print_info(say_hi)()


# In[14]:


@print_info
def say_hi1():
    print('hi')


# In[15]:


say_hi1()


# ### 传递参数

# In[16]:


def print_info1(func):
    
    def wrapper(*args):  # 用 *args（**kwargs） 接收参数
        print(f"start function {func.__name__}")
        func(*args)
        print(f"end function {func.__name__}")
        
    return wrapper


# In[17]:


@print_info1
def say_hi2(name):
    print(f"hi, {name}")


# In[18]:


say_hi2("小心地滑")


# ### 传递返回值

# In[19]:


def print_info2(func):
    
    def wrapper(*args):
        print(f"start function {func.__name__}")
        ret = func(*args)  # 用一个变量 ret 接收返回值
        print(f"end function {func.__name__}")
        return ret  # 完成所有操作以后把 ret 返回
        
    return wrapper


# In[20]:


@print_info2
def add(a, b):
    return a + b


# In[21]:


add(1, 2)


# ## 装饰器的例子

# In[22]:


import time
# 在函数内部定义函数
def timer(func):
    """在不改变函数定义的情况下，改变函数的行为
    """
    
    def wrapper(*args):
        start = time.time()
        ret = func(*args)
        print(f"total tiem for {func.__name__}: {time.time() - start}")
        return ret
        
    return wrapper


# In[23]:


@timer
def long_loop():
    for _ in range(10000000):
        pass


# In[24]:


long_loop()

