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

class Cat(Animal):
    def run(self):
        print('A cat is running...')


print("Is cat an animal?",isinstance(Cat(),Animal))
print("Are animal all cats?",isinstance(Animal(),Cat))

Cat().run()
Cat().run_twice()
#父类的函数调用的同名函数也会被覆盖，是为多态

Dog().run()
