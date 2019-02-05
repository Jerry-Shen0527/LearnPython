def power(x,expo=2):
    result=1
    for a in range(expo):   #用while循环更自然
        result=result*x
    return result

print(power(3))

L=list(range(10))
print(L)

def power3(x):
    return power(x,3)

print(list(map(power3,L)))  #map返回类型为map，要转换为list

from functools import reduce

#首字母大写

def formalize(x):
    return x[:1].upper()+x[1:].lower()  #利用切片大大简化代码(比下标方便许多)

L=['maRy','JERRY',"SAm"]
print(list(map(formalize,L)))

#阶乘功能实现

def multi(x,y):
    return x*y

def Factorial(x):
    return reduce(multi,range(1,x+1))

print(Factorial(10))


#字符串转换

def str2float(x):


    def chartofloat(char):
        pass

    if not isinstance(x,str):
        raise TypeError('bad errand type')
    pass