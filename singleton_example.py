

# class Person:
#     _instance=None
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person._instance=self
 
#     @classmethod
#     def set_age(cls, age, name):
#         cls._instance.age = age
#         cls._instance.name = name
            
# user1=Person("santhosh",25) 
# user2=Person("varun",26)    

# print(user1.age)
# print(user2.age)

# Person.set_age("Ronaldo",30)
# print(user1.name)
# print(user2.name)



class User:
    _instance = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __new__(cls, name, age):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.age = age
        return cls._instance

p1 = User("santhosh", 25)
p2 = User("varun", 26)

print(p1.age) 
print(p2.age)  