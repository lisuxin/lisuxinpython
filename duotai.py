class Animal(object):  # 定义父类，父类本身也继承自Python中的Object类
    def __init__(self, name):
        self.name = name

    def saymyself(self):
        print('In_Animal_class:I am a %s.' % self.name)


class Cat(Animal):  # 定义子类
    def saymyself(self):  # 同名的方法实现不同的功能
        print('In_Cat_class:I am a %s.' % self.name)


class Dog(Animal):  # 定义子类
    def saymyself(self):  # 同名的方法实现不同的功能
        print('In_Dog_class:I am a %s.' % self.name)


class Tiger(Animal):  # 定义子类
    def saymyself(self):  # 同名的方法实现不同的功能
        print('In_Tiger_class:I am a %s.' % self.name)


def testfunc(obj):  # 定义一个调用函数
    print('%s say:' % obj.name)
    obj.saymyself()


animal1 = Animal('animal')
cat1 = Cat('cat')
dog1 = Dog('dog')
tiger1 = Tiger('tiger')

lst = [animal1, cat1, dog1, tiger1]
for i in lst:
    print(i.name)
    testfunc(i)

print(isinstance(animal1, Animal))
print(isinstance(cat1, Animal))
print(isinstance(cat1, Cat))
print(isinstance(dog1, Animal))
print(isinstance(dog1, Dog))
print(isinstance(dog1, Cat))
