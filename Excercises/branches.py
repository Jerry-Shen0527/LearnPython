"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: Jerry
"""

import math

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if (a+b > c and b+c > a and c+a > b):
    print("The length is %f" % (a+b+c))
    p = (a+b+c)/2
    print("The area is %f" % math.sqrt(p*(p-a)*(p-b)*(p-c)))
else:
    print("Not a triangle!")