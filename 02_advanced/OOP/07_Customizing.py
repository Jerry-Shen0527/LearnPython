class Fib(object):
    def __init__(self,num):
        if not isinstance(num,int):
            raise TypeError('Maximum is not an int')
        self.__Maximum=num
        self.__a,self.__b=0,1
    def __str__(self):
        return 'A fibbonacci series ending at {0}'.format(self.__Maximum)
    __repr__=__str__    #repr是为调试服务的，在交互式界面输出的内容

    def __next__(self):
        self.__a,self.__b=self.__b,self.__a+self.__b
        if self.__a>self.__Maximum:
            raise StopIteration('More than Maximum')
        return self.__a
    
    def __iter__(self):
        return self

    def __getitem__(self,n):
        self.__a,self.__b=0,1
        if isinstance(n,int):
            while n>0:
                n=n-1
                self.__a,self.__b=self.__b,self.__a+self.__b
            return self.__a
        
        elif isinstance(n,slice):
            L=[]
            start=n.start
            stop=n.stop
            step=n.step

            if start is None:
                start=0
            if step is None:
                step=1

            for x in range(stop):
                self.__a,self.__b=self.__b,self.__a+self.__b
                if x>=start and ((x-start)%step)==0:
                    L.append(self.__a)

            return L


f=Fib(100)
for a in f:
    print(a)
print(f)

print(f[3])