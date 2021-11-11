#Single Inheritance
#class Base:
#    def fun(self):
  #      print("Base Class")

#class Sub(Base):
   # def fun(self):
     #   print("Sub Class")
    
  #  pass

#ob=Sub()
#ob.fun()


#Multiple Inheritance
class First:
    def __init__(self):
        super(First,self).__init__()
        print("First Class")

class Second:
    def __init__(self):
        super(Second,self).__init__()
        print("Second Class")

class Third(Second,First):
    def __init__(self):
        super(Third,self).__init__()
        print("Third Class")

Third()


#Multi Level Inheritance

#class Animal:
  #  def eat(self):
   #     print("Eating")

#class Dog(Animal):
  #  def bark(self):
   #     print("Barking")

#class BabyDog(Dog):
  #  def weep(self):
  #      print("Weeping")

#d=BabyDog()
#d.eat()
#d.bark()
#d.weep()