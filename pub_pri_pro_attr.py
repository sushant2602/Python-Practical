class Access():

    def __init__(self):
        self.__pri=("I Am Private")
        self._pro=("I Am Protetcted")
        self.pub=("I Am Public")

    def __privateMethod(self):
        print("In Private")

obj=Access()
print(obj.pub)
print(obj._pro)
print(obj._Access__pri)

obj._Access__privateMethod()
