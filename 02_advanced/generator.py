#generator第一种生成
g1=(x*x for x in range(10))
for num in range(10):
    print(next(g1))

#generator函数生成
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

g2=fib(10)  #有yield的函数命名后转换为生成器
print(fib)
print(g2)

for num in range(10):
    print(next(g2))

#拿到返回值
while True:
    try:
        x=next(g2)
        print('g2:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break