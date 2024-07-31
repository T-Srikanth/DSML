# Intermediate DSA: OOPS - 1
###################################################
######### Reference links #########
# https://www.scaler.com/topics/what-is-object-oriented-programming-oop/
# https://www.scaler.com/topics/python/class-in-python/
# https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet
# https://www.interviewbit.com/oops-interview-questions/
# https://www.interviewbit.com/oops-mcq/
# https://www.interviewbit.com/blog/principles-of-oops/
# https://www.interviewbit.com/blog/applications-of-oops/
# https://www.geeksforgeeks.org/encapsulation-in-python/
# https://docs.python.org/3/tutorial/classes.html#inheritance
# https://www.programiz.com/python-programming/polymorphism
####################################################

## Temperature Conversion
# Create a Temperature class that has two methods :
# 1. convertFahrenheit - It will assume that the unit of the given input is celsius and it will convert it into Fahrenheit.
# 2. convertCelsius - It will assume that the unit of the given input is Fahrenheit and it will convert it into celsius.
# The input expected has no unit, it will just be an integer whereas the output has to have a unit of either celsius or Fahrenheit.
class Temperature:
  def __init__(self,val):
    self.val=val
  def convertFahrenheit(self):
    F = (1.8*self.val)+32
    k = round(F,2)
    print("{} degree fahrenheit".format(k))    
    
  def convertCelsius(self):
    C = (5/9) * (self.val - 32)
    m = round(C,2)
    print("{} degree celsius".format(m))
# test = Temperature(32)
# test.convertFahrenheit()
# test.convertCelsius()

## Time conversion
# In the timeConv function, Create a Spanoftime class and initialize it with hours and mins.
# 1. Make a method addTime which should take two Spanoftime objects and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# 2. Make a method returnMinute which should return total minutes in the Spanoftime objects t1 and t2. E.g.- (1 hr 2 min and 1 hr 2 min) should return 124 minute.
def timeConv(a,b,x,y):
  class Spanoftime:
    def __init__(self,hours,mins):
      self.hours = hours
      self.mins = mins

    def displayTime(self):
      return("{} hr : {} min".format(self.hours,self.mins))
    
    def addTime(tm1, tm2):
      h = tm1.hours + tm2.hours + (tm1.mins+tm2.mins)//60
      m = (tm1.mins+tm2.mins)%60
      t_res = Spanoftime(h,m)
      return t_res

    def returnMinute(tm1,tm2):
      return (tm1.hours+tm2.hours)*60 + tm1.mins + tm2.mins
  
  t1 = Spanoftime(a,b)
  t2 = Spanoftime(x,y)
  add_res = Spanoftime.addTime(t1,t2).displayTime()
  min_res = Spanoftime.returnMinute(t1,t2)
  print(add_res)
  print(min_res)
  return add_res
# timeConv(1,1,1,1)