#分段函数
#        3x-5 (x>1)
# f(x) = x+2 (-1<=x<=1)
#        5x+3(x<-1)
"""
x = float(input('x = '))
if x > 1:
    f = 3 * x - 5
elif x >= -1 & x <= 1:
    f = x + 2
else:
    f = 5 * x + 3
print('f(%.1f) = %.2f' % (x,f))
"""

"""
# 百分制成绩转换为等级制成绩
# 90分含90输出A；80-90不含90输出B；70-80不含80输出C；60-70不含70输出D；60以下输出E
score = int(input('百分制分数: '))
if score >= 90:
    g = 'A'
elif score >= 80:
    g = 'B'
elif score >= 70:
    g = 'C'
elif score >= 60:
    g = 'D'
else:
    g = 'E'
print('对应的等级是:',g)
"""

#输入三条边，如果能构成三角形就计算周长和面积
a = float(input('输入边长1：'))
b = float(input('输入边长2：'))
c = float(input('输入边长3：'))
if a + b > c and a + c > b and c + b > a:
    print('可以构成三角形！')
    l = a + b + c
    p = l / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('周长为%.2f面积为%.2f' % (l,area))
else:
    print('不可以构成三角形！')