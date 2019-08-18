"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: Jerry
"""

f = float(input('The Fahrenheit temperature='))
c = (f-32)/1.8
print("%.1f" % c)

"""
输入半径计算圆的周长和面积

Version: 0.1
Author: Jerry
"""

r = float(input("The radius="))
print("The area is %f" % (3.14159*r**2))


"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: Jerry
"""

year = int(input("year="))
print((year % 400 == 0)or(year % 4 == 0 and year % 100 != 0))
