# implement polyphormism with inheritence

class Bird : 
    def intro(self) :
        print("There are many types of birds")

    def flights(self) :
        print("Most of the birds can fly but some of not")

class Sparrow(Bird) : 
    def flights(self): #here method overriding is implemented   
        print("Sparrow can also flight")

class Ostrich(Sparrow) :
    def flights(self):
        super().flights()
        Bird.flights(self)
        print("Ostrich can't fly")
    
bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

bird.intro()
bird.flights()
sparrow.flights()
ostrich.flights()