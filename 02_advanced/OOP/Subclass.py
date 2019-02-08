class Animal(object):
    def run(self):
        print('An animal is running...')
    
    def run_twice(self):
        self.run()
        self.run()

Animal().run()

class Dog(Animal):
    #类内定义的同名函数会覆盖父类的函数
    def run(self):
        print('A dog is running...')
    
    def __len__(self):
        return 100

class Cat(Animal):
    def run(self):
        print('A cat is running...')


print("Is cat an animal?",isinstance(Cat(),Animal))
print("Are animal all cats?",isinstance(Animal(),Cat))

Cat().run()
Cat().run_twice()
#父类的函数调用的同名函数也会被覆盖，是为多态，但其实并不一定需要继承，动态语言的鸭子特性导致只要有run方法就可以正常运行

Dog().run()
