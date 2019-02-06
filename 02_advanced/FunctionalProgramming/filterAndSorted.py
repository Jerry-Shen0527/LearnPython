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

def prime_gen(end):
    yield 2
    it=odd_gen()
    while True:
        n=next(it)
        if n>end:
            raise StopIteration
        yield n
        it=filter(devisible(n),it)
        

#实际上是一种新的思想，在C/C++中筛法是对数组存储的操作，而此处是在不断更新generator的规则

L=[n for n in prime_gen(50)]
print(L)