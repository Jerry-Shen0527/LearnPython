#Class
class Student(object):
    def __init__(self,name,score):
        Student.name=name
        Student.__score=score
#__xxxx__是特殊名称，不能用作private对象的命名
    def set_score(self,newscore):
        if 0<newscore<100:
            self.__score=newscore
        else:
            raise ValueError('Bad score')
    
    def print_status(self):
        print('{0}:{1},GPA={2}'.format(self.name,self.get_score(),self.get_grade()))
    
    def get_score(self):
        return self.__score
    
    def get_grade(self):
        if self.__score>=95:
            return '4.3'
        elif self.__score>=90:
            return '4.0'
        else:
            return 'F'

A=Student('Jerry',98)
A.print_status()

A.name='Tom'
A.print_status()

A._Student__score=70    #强行修改，但不推荐，因为解释器可能会将private对象解释为其他形式
A.print_status()

A.__score=90    #并未修改实例的值，而是对A新建了一个数据
A.print_status()
print(A.__score)

