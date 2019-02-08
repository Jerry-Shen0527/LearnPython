def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>0:
        return x
    else:
        return -x

def my_f(x):
    pass
    print('another function has been used')

# def triple(name='Jerry',son):     #默认参数要后置
#     input("name of son:")
#     return name,son  #python允许多值返回，但事实上返回了一个元组

def add_end_wrong(L=[]):
    L.append('end')
    return L

def add_end_right(L=None):  #默认形参用不可变对象
    if not L:
        L=[]
    L.append('end')
    return L

# print(add_end_right())
# print(add_end_right())
# print(add_end_right())

def sum(*num):
    result=0
    for number in num:
        result+=number
    return result

L=[1,2,3]

print(sum(*L))  #类似指针的取内容

def sumagain(*num,a):
    print(a,num)

sumagain(3,6,a=2)   #定义原型：func(参数，默认参数，可变参数，关键字参数，命名关键字参数)

def keyword(name,age,**kw):
    print(name,age,kw)

keyword('Jerry',18,city='Hefei',single=True)

def f1(a,b,c,*args,d,**kw):
    print('a={0} b={1} c={2},d={3},args={4},kw={5}'.format(a,b,c,d,args,kw))

f1(1,2,3,4,dd=6,fuck=100,d=5)
