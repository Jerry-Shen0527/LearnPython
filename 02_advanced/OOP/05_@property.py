class Student(object):
    
    @property
    def score(self):
        return self.__score
    
    @score.setter   #与@property同步创建
    def score(self,num):
        if not isinstance(num,int):
            raise TypeError('the number should be an int')
        if num>100:
            raise ValueError("more than 100!")
        elif num>60:
            self.__score=num
        elif num>0:
            self.__score=num
            print('You failed!')
        else:
            raise ValueError("less than 0")

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,num):
        if not isinstance(num,int):
            raise TypeError('not an int')
        if not num<=2019:
            raise ValueError('born too late')
        self._birth=num

    @property   #是一个只读属性
    def age(self):
        return 2019 - self._birth


A=Student()
A.score=70
A._score=110
print(A.score)

A.birth=2008
print(A.age)

class Screen(object):
    @property
    def width(self):
        return self.__height

    @width.setter
    def width(self,num):
        if not isinstance(num,int):
            raise TypeError('width resolution should be an int')
        if num>1920:
            raise ValueError('bigger than full screen')
        self.__width=num
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,num):
        if not isinstance(num,int):
            raise TypeError("height resolution should be an int")
        if num>1080:
            raise ValueError("too high")
        self.__height=num

    @property
    def resolution(self):
        return self.__height*self.__width


s=Screen()
s.width=1280
s.height=720
print(s.resolution)