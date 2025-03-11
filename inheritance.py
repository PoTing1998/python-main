class People :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping....")
    
    def eat(self):
        print(f"{self.name} is eating....")

class Student(People): 
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def eat(self,food):
        print(f"{self.name} is now eating {food}")

student1 = Student("John", 20, 1234)

student1.eat("pizza")