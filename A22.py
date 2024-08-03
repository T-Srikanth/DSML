# Intermediate DSA: OOPs - 2
###################################################
######### Reference links #########
# https://hackmd.io/@scaler-topics-main/Skg5Z7bec
# https://docs.google.com/document/d/1-V2IODflbw1si6-egSCmngGiAINbhkmLgOgeaYtmXFA/edit#
# https://hackmd.io/@scaler-topics-main/HyhYhGa15
# https://en.wikipedia.org/wiki/Single-responsibility_principle
####################################################

## OOPs in Python
# You are already given a class Animal with its constructor and a method. You have to define a class Dog which will inherit the Animal class with the following data members and methods:
#   Data Members:
#     name: string
#     breed: string
#   Methods:
#     Constructor: Initialize the data member and call the parent class constructor
#     getname(): Returns the data member name.
#     getbreed(): Returns the data member breed.
#     sound(): Prints 'Dog Barks'.
# You have to define a class Cat which will also inherit the Animal class with the following data members and methods:
#   Data Members:
#     name: string
#     breed: string
#   Methods:
#     Constructor: Initialize the data members.
#     getname(): Returns the data member name.
#     getbreed(): Returns the data member breed.
#     sound(): Prints 'Cat Meows'.
# In the main function() create instances for each object and call the sound function for that instance just after its initiation in the order Animal, Dog and Cat. 
# Firstly an animal instance is made then its sound is called and continue with this pattern with other objects in the mentioned order.
class Animal:
  def __init__(self):
    print("Animal is Here")
  def sound(self):
    print("Animal Sounds")

class Dog(Animal):
  def __init__(self,name,breed):
    super().__init__()
    self.name = name
    self.breed = breed
  def getname(self):
    return self.name
  def getbreed(self):
    return self.breed
  def sound(self):
    print("Dog Barks")

class Cat(Animal):
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
  def getname(self):
      return self.name
  def getbreed(self):
      return self.breed
  def sound(self):
      print('Cat Meows')
def main():
  animal = Animal()
  animal.sound()
  dog = Dog('Olaf','GR')
  dog.sound()
  cat = Cat('puttu','street')
  cat.sound()
# main()

## Bus Class
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seatingcapacity() a default value of 50.
# The inputs are the name, mileage and max speed for an instance and the output is expected as the following:
# "The seating capacity of a {name} with maxspeed {max_speed} and mileage {mileage} is {capacity}" ,for which the code is included in the solution prefix.
class Vehicle:
  def __init__(self,name,mileage,max_speed):
    self.name = name
    self.mileage = mileage
    self.max_speed = max_speed
class Bus(Vehicle):
  def seatingcapacity(self):
    self.sc = 50
    print("The seating capacity of a {} with maxspeed {} and mileage {} is {}".format(self.name,self.max_speed,self.mileage,self.sc))
# bus =  Bus('BUS','15kmpl','60kmph')
# bus.seatingcapacity()
  