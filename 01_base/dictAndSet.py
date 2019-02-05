d={'Micheal':95,'Jerry':113,'Lucy':70}  #大括号扩起表示是dictionary
print(d['Jerry'])
d['Cauchy']=109
print(d['Cauchy'],d.pop('Lucy'),d.get('Lucy'))
a=360
d[a]=[555,666]    #无法使用列表作为key,但是元组可以,元组内不能有可变对象
print(d[360])
print(d.get('Micheal'),d.get('Mary'))

#dict函数和zip函数
L1=[1,2,3,4,5]
L2=[1,1,23,4,5,6,8,9]
L3=list(range(10))

D1=dict(zip(L1,L2))  #zip对象可以用来创建dict
D2=dict(a=1,b=2,c=3)
D3=dict([(1,2),(3,4),(5,6)])
print(D3)

Z=zip(L1,L2,L3)
Zinverse=zip(*Z)    #zip对象只能调用一次，第二次会失去值

print(list(Z))
print('Z*:',list(Zinverse))

s=set([1,2,3,4,4,4,4,4])    #接受list作为参数，可以用range返回
s.add(-1)
s.remove(2)
print(s)
s2=set([1,3,5,7,9])
print(s&s2)     #可以有集合的运算操作，只能存储不可变对象