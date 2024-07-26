# creating a class
class Main : 
    # class variable or static variable
    res = 0
    # constructor
    def __init__(self): 
        print("Welcome to constructor")
    
    def add(self , n1 , n2) :
        self.res = n1 + n2
        
    def output(self) : 
        # instance var
        x = 0
        
        print(self.res)
        

# main is an instance of class Main
main = Main()
# print(main.name)
main.add(9,1)
main.output()

class Add : 
    def __init__(self , n1 , n2) :
        z = n1 + n2
        print(f"addition of {n1} and {n2} is" , z)
        
Add(2,3)