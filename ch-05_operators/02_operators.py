# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# Arithmetic -> exponential

a = 2
b = 3
c = a**b
print(a , "to the power" , b , "is",c)

# Arithmentic -> Modulus Used for reminder
num1 = 10
num2 = 4
reminder = num1 % num2
print(f"reminder of {num1} and {num2} is {reminder}")

# Arithmetic -> floor division
n1 = 15
n2 = 2
res = n1//n2
print(f"The floor value is {res}")

# Identity operator -> x is y , x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Membership operators -> in , not in
print("Some membership operator example\n\n")
x = ["apple", "banana"]

print("banana" in x)
print("apple" in x)
print("apple" not in x)
