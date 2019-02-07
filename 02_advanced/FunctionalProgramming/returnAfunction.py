#类似C++中函数指针的作用（C++中函数名即为指针）


#闭包函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*arg):
    def sum():
        result=0
        for i in arg:
            result=result+i
        return result
    return sum

f=lazy_sum(1,3,5,7,9)   #此时f并没有被调用，但数组已经被保存
print(f())

#循环变量的使用：尽量别用

def count():
    L=[]
    for i in range(1,4):
        def f():
            return i*i
        L.append(f)
    return L

f1,f2,f3=count()

print(f1(),f2(),f3())   #统一被调用时，i都已经变成了3

def power(n):
    return lambda x:x**n

print(power(3)(4))