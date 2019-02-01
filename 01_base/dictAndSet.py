# d={'Micheal':95,'Jerry':113,'Lucy':70}  #大括号扩起表示是dictionary
# print(d['Jerry'])
# d['Cauchy']=109
# print(d['Cauchy'],d.pop('Lucy'),d.get('Lucy'))
# a=360
# d[a]=[555,666]    #无法使用列表作为key,但是元组可以,元组内不能有可变对象
# print(d[360])

s=set([1,2,3,4,4,4,4,4])    #接受list作为参数，可以用range返回
s.add(-1)
s.remove(2)
print(s)
s2=set([1,3,5,7,9])
print(s&s2)     #可以有集合的运算操作，只能存储不可变对象