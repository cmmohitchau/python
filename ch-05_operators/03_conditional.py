a = 7
b = 4

if a==b :
    print("a is equal to b")
else :
    print("a is not equal to b")
    
# elif

# age = int(input("Enter your age\n"))

# if age < 18 :
#     print("You are child")
# elif age >= 18 and age <= 30 :
#     print("You are young")
# elif age > 30 and age <= 60 :
#     print("You are in your middle life")
# else :
#     print("You are an old")
    
    # nested if
# wap for entry in girls college if she is girls and above or equl to 18

gender = input("Enter your gender f for female and m for male\n")

if gender == "f" :
    age = int(input("Enter your age\n"))
    if age >= 18 :
        print("You are welcome to the hostel")
    else :
        print("Your age is not enough to get entry in the hostel")
else :
    print("You are not female so you can't enter in the hostel")