# In lambda no return keyword and always have parameters

Add = lambda X,Y : X+Y

print(Add(2,3))

class Main : 
    def __init__(self) :
        self.add = lambda x,y : x + y
        self.multiply = lambda x,y : x * y

main = Main()

print(main.add(4,5))
print(main.multiply(4,5))
print(main.add(9,8))