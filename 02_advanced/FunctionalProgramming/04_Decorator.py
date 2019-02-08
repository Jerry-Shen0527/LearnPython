#装饰器为函数添加新功能

#不带参数

def log(func):
    def wrapper(*argv,**karg):
        print('"{0}" function is running:'.format(func.__name__))
        return func(*argv,**karg)
    return wrapper

@log
def now():
    print('2019.2.7')

f=now
print(now.__name__)
print(f.__name__)   #名字相同

print(now.__name__)
now()

#带参数

def log_t(text):
    def decorator(func):
        def wrapper(*arg,**karg):
            print('Message:{0},{1}is running'.format(text,func.__name__))
            return func(*arg,**karg)
        return wrapper
    return decorator

@log_t('Warning:')
def tommorrow():
    print('2019.2.8')

tommorrow()

#加上修饰器后，函数的__name__对象变成了wrapper。但不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
import functools

def log_Name(func):
    @functools.wraps(func)
    def wrapper(*arg,**karg):
        print('call function "{0}"'.format(func.__name__))
        return func(*arg,**karg)
    return wrapper  

@log_Name
def fuck(x):
    while x>0:
        print('fuck')
        x=x-1

print(fuck.__name__)
fuck(5)

#Practice:请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

def metric():
    pass