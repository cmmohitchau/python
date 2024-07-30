# ._ is protected member which can be accessed within class and its derived class
# .__ is private member which can only accessed within its class

class Base :
    def __init__(self) :
        self.a = 6
        self._b = 3
        print(self._b)
        self.__c = 9
        print("in base class" , self.__c)

class Child(Base) :
    def __init__(self) :
        super().__init__()
        print(self._b)

child = Child()

