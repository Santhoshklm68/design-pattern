# import pydantic
# from typing import Optional

# class User(pydantic.BaseModel):
#     name : str
#     age : int
#     email : Optional[str] = None
#     phone_number: Optional[str] = None
    
#     @pydantic.validator('name')
#     @classmethod
#     def name_valid(cls,value):
#         if len(value) < 3:
#             raise ValueError("Name must be atleast 3 characters")
#         return value
#     def age_valid(cls,value):
#         if value is str:
#             raise ValueError("Age must be an integer")
#         return value
            
    
    
# user1 = User(name="Santhosh", age="ssvj", email="santhoshklm68@gmail.com", phone_number="6380526174")
# print(user1)
# print(user1.name)
class CarSingleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.make = args[0]
            cls._instance.model = args[1]
            cls._instance.year = args[2]
            cls._instance.odometer_reading = 0 
        return cls._instance

    def get_descriptive_name(self):
        """Return a descriptive name of the car."""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Update the odometer reading.
        Reject the change if it attempts to roll back the mileage.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't decrease mileage by incrementing odometer!")


my_car1 = CarSingleton("Toyota", "Camry", 2020)
my_car2 = CarSingleton("Honda", "Civic", 2021)
my_car3 = CarSingleton("innova", "crysta", 2024)

print(my_car2 is my_car3)  

print(my_car2.get_descriptive_name())
my_car1.read_odometer()
print(my_car3.get_descriptive_name())
print(my_car2.get_descriptive_name())

my_car1.update_odometer(5000)
my_car1.read_odometer()
my_car1.increment_odometer(100)
my_car1.read_odometer()
