class Edureka:
    def __init__(self,coursename):
        self.coursename=coursename
    def setcourse_Name(self,coursename):
        self.coursename=coursename
    def getcourse_Name(self):
        return(self.coursename)

ob=Edureka("Python")
print(ob.getcourse_Name())

ob.setcourse_Name("Machine Learning")
print(ob.getcourse_Name())