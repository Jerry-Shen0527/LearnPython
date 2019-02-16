#动态绑定方法
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
        self.public='Public'
    def set_score(self,new):
        self.__score__=new
    
    def status(self):
        print(self.__name,':',self.__score,self.public)

A=Student('Jerry',100)
A.status()
B=Student('Mary',120)
from types import MethodType

def republic(self):
    self.public='Changed public'

B.status()

B.republic=MethodType(republic,B)
B.republic()

B.status()

# A.republic()  此处只给B绑定了方法，A则无法调用
Student.republic=republic

A.status()
A.republic()
A.status()

#使用__slots__
class Refrained(object):
    __slots__=('name','age')

C=Refrained()
C.name='Micheal'
C.age=100
# C.score=50  #插槽被限制了

class SubRefrained1(Refrained): #子类没有slots对象时，则没有了限制
    pass

D=SubRefrained1()
D.score=100

class SubRefrained2(Refrained): #子类有自己的slots时，新的slots则是并集
    __slots__=("score")

E=SubRefrained2()
E.score=100
E.gender='M'
