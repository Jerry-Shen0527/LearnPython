class Animal(object):
    pass


class Runnable(Animal):
    def run(self):
        print("Running......")

class Flyable(Animal):
    def fly(self):
        print("Flying......")


class Mammal(Animal):
    pass
class Bird(Animal):
    pass


class Cat(Mammal,Runnable):
    pass
class Dog(Mammal,Runnable):
    pass


class Emu(Bird,Runnable):
    pass
class Parrot(Bird,Flyable):
    pass

D=Dog()
D.run()
#我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。