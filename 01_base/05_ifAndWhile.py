#Flat is better than nested

year = int(input('your birthyear:'))
if year < 2000:
    print('old')
    print('the month is %d' % int(input('which month?')))
else:
    print('young')



"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: 骆昊
"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))


classmates = ['Jerry', 'Micheal', 'Lucy']
for name in range(3, 6):  # range函数返回一个列表或元组
    a = name
print(a)

a = 1
while a < 100:
    a *= a+1
print(a)
