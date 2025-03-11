# class Robot:
#     #in class ,we can also define doctring
#     """Robot class  is for creating robots"""
#     ingredients = "metal"

#     #constructor
#     def __init__(self, inputName,inputAge):
#         self.name = inputName
#         self.age = inputAge
#     def walk(self):
#         print(f"{self.name} is walking.")
#     def sleep(self,hours):
#         print(f"{self.name} is goting to sleep for {hours} hours.")
#     def greet(self):
#         print(f"Hello, my name is {self.name},and I am made of {self.__class__.ingredients}")
# my_robot = Robot("R2D2", 10 )
# # print(my_robot.__doc__)
# my_robot.walk()
# my_robot.sleep(10)
# my_robot.greet()



class  Circle:
    pi = 3.14159
    all_circles = []
    def __init__(self,radius):
        self.radius = radius
        self.__class__.all_circles.append(self)
    def area(self):
        return self.__class__.pi*(self.radius**2)
    
    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total
    @classmethod
    def total_area_2(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total
    

    # 主要是因為改了class 的名稱之後 這個staticmethod 也要改 裡面的class 名稱，但是 classmethod 就不用 降低了耦合度
c1 = Circle(1)
# print (c1.area())
# print(c1.__class__.total_area())
print(c1.__class__.total_area_2())

#note 其實很多class method都可以寫成一般的method。但class method的好處在於，class method屬於這個class，所以我們透過class來instantiate objects時，每個object佔用的記憶體會更少。

# 假定某個class有10個method以及3個class method，那麼我們instantiate 100個objects時，會用到的記憶體量是100 x 10 = 1000單位。

# 但如果我們不用class method，全寫成一般的method，那麼我們instantiate 100個objects時，會用到的記憶體量是100 x 13 = 1300單位。

# 因此，如果我們知道某個method可以寫成class method，就應該要這麼做，節省記憶體用量。另外，對程式節省記憶體是很重要的。