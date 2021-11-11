class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    
    @classmethod
    def dmy(ob1,day,month,year):
        ob1.year=year
        ob1.month=month
        ob1.day=day
        #order of return should be same as init
        return ob1(ob1.year,ob1.month,ob1.day)
    
    @classmethod
    def mdy(ob2,month,day,year):
        ob2.year=year
        ob2.month=month
        ob2.day=day
        #order of return should be same as init
        return ob2(ob2.year,ob2.month,ob2.day)
    
    def __del__(self):
        print("Destructor has been called")

a=Date(2000,3,18)
print("year is "+str(a.year)+", Month is "+str(a.month)+", Day is "+str(a.day))

b=Date.dmy(26,2,1998)
print("\nDay is "+str(b.day)+", Month is "+str(b.month)+", Year is "+str(b.year))

c=Date.mdy(10,15,1994)
print("\nMonth is "+str(c.month)+", Day is "+str(c.day)+", Year is "+str(c.year))