def power(x,expo=2):
    result=1
    while expo>0:
        result=result*x
        expo=expo-1
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

    flag=False
    times=0
    DIGITS=dict(zip(list('0123456789'),range(10)))

    def chartofloat(char):
        nonlocal flag
        nonlocal times
        if flag==True:
            times=times+1
            return DIGITS[char]
        else:
            return DIGITS[char]

    if not isinstance(x,str):
        raise TypeError('bad errand type!')
    
    def combine(x,y):
        nonlocal flag
        if not isinstance(x,int):
            x=chartofloat(x)
        if y=='.':
            if flag:
                raise TypeError('input is not a float') #检查输入是否合规
            flag=True
            return x
        return x*10+chartofloat(y)
       
    return reduce(combine,x)/10**times

print(str2float('0.456'))