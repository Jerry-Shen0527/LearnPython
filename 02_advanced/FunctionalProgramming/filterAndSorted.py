#filter
F=filter(lambda x:x%2==0,list(range(10)))
print(next(F))

#求素数
def odd_gen():
    n=3
    while True:
        yield n
        n=n+2

def devisible(n):   #返回函数：函数的高级操
    return lambda x:x%n>0

def gen_prime(end):
    yield 2
    it=odd_gen()
    while True:
        n=next(it)
        if n>end:
            raise StopIteration
        yield n
        it=filter(devisible(n),it)
        

#实际上是一种新的思想，在C/C++中筛法是对数组存储的操作，而此处是在不断更新generator的规则

#sorted与sort的区别：sorted会返回一个新的list，sorted的参数是Iterable,而sort只能对list进行操作
print(sorted([5,7,3,1,-5],reverse=True,key=abs))        #默认升序，关键词为处理函数

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
D=dict(L)
print(D)
print(sorted(L,key=(lambda x:x[1])))    #直接返回被迭代的对象
print(sorted(D.items()))        #items返回元组
print(sorted(D))        #默认返回dict.keys
