# 找出水仙花 每个位上数字的立方之和正好等于它本身
"""
for x in range(100,10000):
    d = x // 1000 % 10
    c = x // 100 % 10
    b = x // 10 % 10
    a = x % 10
    if a ** 3 + b ** 3 + c ** 3 + d ** 3 == x:
        print('%d是水仙花' % x)
"""
# 正整数反转
"""
num = int(input('输入数字:'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
"""
"""
# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块买100只鸡，问公鸡、母鸡、小鸡各有多少只
for x in range(0,20):
    for y in range(0,33):
        z = 100 - x -y
        if 5*x+3*y+z/3==100:
            print('公鸡有%d只，母鸡有%d只，小鸡有%d只' % (x,y,z))
"""
# CRAPS赌博游戏：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，
# 玩家继续要骰子，直到分出胜负
# 假设你有1000元
"""
from random import randint

money = 1000
first = 1
print('你的资产为：%d' % money)
while money > 0:
    while True:
        zhu = int(input('请下注：'))
        if zhu <= money and zhu > 0:
            break
    pd = True
    num = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % num)
    while pd:
        if first == 1 & (num == 7 or num == 11):
            money += zhu
            print('玩家赢')
            pd = False
            break
        elif first == 1 & (num == 2 or num == 3 or num == 12):
            money -= zhu
            print('玩家输')
            pd = False
            break
        else:
            pd = True
            num1 = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % num1)
            if num1 == 7:
                money -= zhu
                print('玩家输')
                pd = False
                break
            elif num1 == num:
                money += zhu
                print('玩家赢')
                pd = False
                break
        first += 1
    if  money <= 0:
        print('您破产了！')
    print('你的剩余资产:%d' % money,end='\n')
    con = int(input('继续请按1，结束请按0：'))
    if con == 0:
        break
"""

# 生成斐波那契数列的前20个数
"""
num1 = 1
num2 = 1
for x in range(10):
    print('%d' % num1,end='\t')
    print('%d' % num2, end='\t')
    num3 = num1 + num2
    num1 = num2 + num3
    num2 = num1 + num3
    print('%d' % num3, end='\t')
"""
# 找出1000以内的完美数
# 所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身
"""
for x in range(2,10000):
    num = 0
    for i in range(1,x):
        if x % i == 0:
            num += i
    if num == x:
        print('%d是完美数' % x,end='\t')
"""

# 找出100以内所有的素数
for x in range(2,1000):
    if x == 2:
        print('%d' % x, end='\t')
    for i in range(2,x):
        if i == x -1:
            print('%d' % x,end='\t')
        if x % i == 0 & i != 1:
            break
