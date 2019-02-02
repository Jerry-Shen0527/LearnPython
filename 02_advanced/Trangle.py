def Yang(max):
    L=[1]
    for x in range(max):
        yield L
        L2=[0,*L]
        for i in range(1+x):
            L2[i]=L2[i]+L[i]
        L=L2
    return 'done'

gen=Yang(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))