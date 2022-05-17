class Car:
    __distance = 0  # 私有类属性

    def __init__(self, name):
        self.__name = name
        Car.__distance += 1

    def show(self):
        print("self.__name", self.__name)
        print("Car.distance", Car.__distance)

    @classmethod  # 修饰器声明类方法，类方法是类所拥有的方法，第一个参数必须是类对象一般将cls作为类方法第一个参数名称，调用该方法时不需要传值
    def classShowdistance(cls):
        print(cls.__distance)

    @staticmethod  # 修饰器，修饰静态方法
    def staticShowmethod():
        print(Car.__distance)


car1 = Car('passat')
print(car1.classShowdistance())
print(car1.classShowdistance())
print(car1.show())
car2 = Car('benz')
print(Car.classShowdistance())
print(Car.classShowdistance())
print(Car.show(car1))
print(Car.show(car2))