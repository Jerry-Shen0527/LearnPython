classmates=['Jerry','Tom','Micheal']
print(len(classmates),classmates[0],classmates[-1],classmates[-3])
classmates.insert(2,'Jack')
classmates.append('Mary')
print(classmates[2],classmates[-1])
print(classmates.pop(-2))
print(classmates)
house=['Jerry','Mouse',3,['sofa','desk','chair']]   #中括号内部为list，定义有多种方法，元素可变，且不要求元素为同种
print(house[-1][-1])

city=('Wuhan','Lanzhou','Hefei')    #小括号内部为元组，内容不可变，类似int const*
print(city[-1])