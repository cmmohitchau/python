def table(num , index) :
    print(num , "*" , index , "=" , num*index)
    if index < 10 : table(num , index + 1)
    else : print("Thank you !")
    


def App() :
    num = int(input("Enter a number \n"))
    table(num , 1)
    
App()