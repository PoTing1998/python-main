class Robot:
    def __init__(self, name, age,address):
        self.name = name
        self.age = age
        self.address = address

        #define a private method __key()
    def __key(self):
        return (self.name, self.age, self.address)
        
        #implememnt __hash__() function
    def __hash__(self):
        return hash(self.__key())
        
    def __eq__(self, other):
        if  isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented
    
    def __str__(self):
        return f"Robot({self.name} is now {self.age} years old, living in {self.address})"
    def __repr__(self):
        return f"Robot({self.name},{self.age},{self.address})"
    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented
    
    def __gt_(self , other):
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented
        
robot1 = Robot('Alice', 25, 'New York')
robot2 = Robot('Grace', 34, 'New York')

print(robot1 == robot2)

class Robot:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address
    
    # define a private function
    def __key(self):
        return (self.name, self.age, self.address)

    def __hash__(self):
        return hash(self.__key())
    
    def __eq__(self, other):
        return self.__key() == other.__key()



robot = Robot("Wilson", 25, "Hawaii")
dictionary = {robot: "W robot"}
print(dictionary[robot]) #return W robot