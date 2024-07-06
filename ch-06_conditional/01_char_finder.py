def printFirstChar(String) :
    if String :
        print(String[0])
    else :
        print("plz Enter any String first")

def printLastChar(String) :
    if String :
        print(String[len(String) - 1])
    else :
        print("plz Enter any String first")
        
def printCustomChar(String) :
    index = int(input("Enter any index starting from 0\n"))
    
    if index <= len(String) - 1 :
        print(String[index])
    else :
        print("Your index in not in the range")
        
    
def App() :
    String = input("Enter any string\n")
    print("You have entered" , String)

    print("1. for choosing first character")
    print("2. for choosing second character")
    print("3. for choosing custom character")

    option = input("Enter option\n")

    if option == "1" :
        printFirstChar(String)
    elif option == "2" :
        printLastChar(String)
    else :
        printCustomChar(String)
        
App()