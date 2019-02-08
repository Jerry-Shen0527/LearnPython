L=list(range(1,100,5))

print(L)
print(L[7:10],L[::3])

T=tuple(range(1,100,5))
print(T[3:5],T[-3:],T[-1])  #从负数开始省略时，默认到-1(倒数第一个)

print('hello world!'[:5])

D={'A':1,'B':2,'C':3}

for key in D:
    print(key)
for Value in D.values():    #返回值的列表
    print(Value)
for item in D.items():  #返回key-value的tuple
    print(item)

from collections import Iterable
print(isinstance('a',Iterable))
print(isinstance(33333,Iterable))
E=enumerate(L)
print(type(E))
for x,y in D.items():
    print(x,y)
for x in E:
    print(x)