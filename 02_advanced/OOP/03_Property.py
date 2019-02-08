#type()方法
from Subclass import Animal

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