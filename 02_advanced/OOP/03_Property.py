#type()方法
from Subclass import *

print(type(123))
print(type('hello world'))
print(type(Animal()))

#type()函数返回对应的class类型
print(type('hello')==str)
print(type(123)==int)

#函数类型的扩展
import types
def test():
    pass
print('Testing the extensive types:')
print(type(x*x for x in range(10))==types.GeneratorType)
print(type(test)==types.FunctionType)
print(type(lambda x:x*x)==types.LambdaType)

#isinstance()方法:在Subclass文件中已经有体现
print('testing isinstance')
print(isinstance(b'a',bytes))
#isinstance的第二个参数还可以接受可变参数
print(isinstance((1,2,3),(list,tuple)))
print(isinstance([1,2,3],(list,tuple)))


#dir()方法

print('testing Dir()')
print(dir(Dog()))
print(len(Dog()))
#等价写法
print(Dog().__len__())

print(dir('ABC'))   #返回类中定义的所有方法

print('testing my object:')
class MyObject(object):
    def __init__(self):
        self.x=3
    def power(self):
        return self.x*self.x

obj=MyObject()
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
print(getattr(obj,'x'))
print(getattr(obj,'y',404))     #传入默认参数，若不存在则返回默认值
setattr(obj,'x',9)
print(getattr(obj,'x'))
f=getattr(obj,'power')
setattr(obj,'x',5)
print(f())  #此处f仅仅为一个指向函数的指针，因此改变实例存储的值时，再调用函数，结果也会改变