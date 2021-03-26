#将华氏温度转换为摄氏温度
# f = float(input('请输入华氏温度：'))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f,c))

# 输入圆的半径计算周长与面积
# r = float(input('圆的半径:'))
# l = 2 * r * 3.1416
# a = 4 * 3.1416 * (r**2)
# print('半径为%.2f的圆的周长为%2.f面积为%2.f' % (r,l,a))

# 输入年份判断是不是闰年
year = int(input('输入年份：'))
if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
    is_year = 1
else:
    is_year = 0
print(is_year)