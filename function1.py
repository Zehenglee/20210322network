# import this
# import sys
# print(sys.version_info)
# print(sys.version)
"""
import turtle

turtle.pensize(4)
turtle.pencolor("red")

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()
"""
"""
# 定义函数
def fac(num):
    # 求阶乘
    result = 1
    for n in range(1,num + 1):
        result *= n
    return result
n = int(input('n = '))
m = int(input('m = '))
print(fac(m)//fac(n)//fac(m - n))
"""
"""
# 定义一个函数可以有多种不同的使用方式
from  random import  randint

def roll_dice(n=2):
    # 摇色子
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0,b=0,c=0):
    # 三个数相加
    return a+b+c

# 如果没有指定参数，默认摇两颗色子
print(roll_dice())
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=3,b=5,a=9))
"""
"""
# 在参数名前面的*表示args是一个可变的参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add())
print(add(1))
print(add(1,2))
print(add(1,4,2,6,4))
"""
"""
# function_module1.py和function_module2.py两个模块里面都有foo函数
# 在主函数里面调用时可以用下面的方式进行区分
import function_module1 as n1
import function_module2 as n2

n1.foo()
n2.foo()
"""
"""
# 如果写成以下形式会因为后导入的覆盖前导入的
from function_module1 import foo
from function_module2 import foo

foo()
"""

# python解释器在导入这个模块时就会执行这些代码，
# 事实上我们可能并不希望如此，因此如果我们在模块
# 中编写了执行代码，最好是将这些执行代码放入如下
# 所示的条件中，这样的话除非直接运行该模块，if条
# 件下的这些代码是不会执行的，因为只有直接执行的
# 模块的名字才是"__main__"

import  function_module3
#  导入module3时 不会执行模块中if条件成立时的代码
#  因为模块的名字是module3而不是__main__

# 实现计算求最大公约数和最小公倍数的函数
def gcd(x,y):
    if x>y:
        max_num = x
        min_num = y
    else:
        max_num = y
        min_num = x
    for i in range(min_num,0,-1):
        if max_num % i == 0 and min_num % i == 0:
            return i

def lcm(x,y):
    return x * y //gcd(x,y)
# 实现判断一个数是不是回文数的函数
def huiwenshu(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10+ temp % 10
        temp //= 10
    return num == total

# 实现判断一个数是不是素数的函数
def sushu(num):
    for n in range(2,int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True if num != 1 else False

# 写一个程序判断输入的正整数是不是回文素数
if __name__ == '__main__':
    num = int(input('请输入正整数：'))
    if sushu(num) and huiwenshu(num):
        print('%d是回文素数' % num)
    else:
        print('%d不是回文素数' % num)

# 基本格式
def main():
    # Todo:Add your code here
    pass

if __name__== '__main__':
    main()