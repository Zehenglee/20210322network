"""
# for-in 循环
# range(101)可以产生一个0到100的整数序列
# range(1,100)可以产生一个1到99的整数序列
# range(1,100,2)可以产生一个1到99的奇数序列，步长为2
sum = 0
for x in range(0,101,2):
    sum += x
print(sum)
"""

# while循环
# 猜字游戏：计算机随机出一个1-100之间的随机数，由人来猜
# 计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import  random

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('再大一点')
    elif number > answer:
        print('再小一点')
    else:
        print('恭喜猜对啦！')
        break
print('你一共猜对了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
"""

# 输出九九乘法表
"""
for i in range(1,10):
    for j in range(1,i + 1):
        if i == j:
            print('%d * %d = %d' % (j,i,j*i),end='\n')
        else:
            print('%d * %d = %d' % (j, i, j * i), end='\t')
"""
"""
#判断输入的正数是不是素数
b = 0;
number = int(input('输入正数：'))
if number == 1:
    b = 1
elif number == 2:
    b = 0
else:
    for x in range(2,number):
        if number % x == 0 and number > 1:
            b = 1;
            break
if b == 1:
    print('不是素数')
else:
    print('是素数')
"""

# 输入两个正整数，计算它们的最大公约数和最小公倍数
"""
a = int(input('输入正整数a='))
b = int(input('输入正整数b='))
if a < b:
    max_num = b
else:
    max_num = a
for x in range(max_num,0,-1):
    if a % x == 0 & b % x == 0:
        print('%d和%d的最大公约数是%d' % (a,b,x))
        print('%d和%d的最小公倍数是%d' % (a,b,a * b // x))
        break
"""

# 打印三角形图案
row = int(input('请输入行数：'))
for i in range(row):
    for j in range(i + 1):
        print('*',end='')
    print()

for i in range(row):
    for j in range(row):
        if j >= row - i - 1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

for i in range(row):
    for j in range(row-1-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()