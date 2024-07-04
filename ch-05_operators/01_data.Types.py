
# intro of seperator
def add() :
    firstNumber = int(input("Enter your first number "))
    secondNumber = int(input("Enter your second number "))
    result = firstNumber + secondNumber
    print("Sum of ", firstNumber ," + " , secondNumber ," is " ,result , sep="")
    
add()


# checking data type

# int 
# string
# bool
# Set
# None
def checkDataType() :
    data = "hi"
    dataType = type(data).__name__
    print("Your data type is" , dataType)

checkDataType()