# Create a file named method_override.py 

# takes inputs that asks for the name,age,hair colour,and eye colour of a person  
name = input("name:")
age = int(input("age:"))
hair_colour = input("hair_colour:")
eye_colour = input("eye_colour:")
    
# Created a Parent Class and assigned a can drive method to it    
class Parent ():
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name 
        self.age = age 
        self.eye_colour = eye_colour 
        self.hair_colour = hair_colour
    
    def can_drive(self):
        print(f"{self.name} is old enough to drive")
        

# Created a sub class that copys the method of the Parent class 
# craeted a can drive method 
class Child(Parent):
    def __init__(self, name, age, eye_colour, hair_colour):
        
        super().__init__(name, age, eye_colour, hair_colour) 
        
    def can_drive(self):
        print(f"{self.name} is to young too drive")
   
# conditional statements used to determine if a person is the right age to drive      
if age >= 18:
    Person = Parent(name, age , hair_colour, eye_colour)
else:
    Person = Child(name , age , hair_colour , eye_colour)
 
 # calling the can drive method to execute
Person.can_drive()
    
    

    

        
        
        
        
        