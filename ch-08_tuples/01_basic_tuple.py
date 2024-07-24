# Tuple items are ordered, unchangeable, and allow duplicate values.
# If you want to add or delete you can convert it into list and perform those operation

tup1 = ("mohit" , "rohit" , "hari" , "ram")
tup2 = ("hari","sit","hanuman","krishna")
print(type(tup2).__name__)

# membership operation

if "rohit" in tup1 :
    print("Yes it is present in the tup1")
    
tup1 += tup2
print(tup1)

# converting to list

list1 = list(tup1)
print(list1)
list1.insert(2,"shyam")
print(list1)
tup1 = tuple(list1)
print(tup1)

# deleting tup1

# del tup1
# print(tup1)

# unpacking tuple
fruits = ("mango" , "apple" , "grapes" , "banana")

# (yellow , red , green) = fruits
# print(type(yellow).__name__)
# print(red)

# using * we can store more than one element in one var
(yellow , *red) = fruits

print(yellow)
print(red)

# count and index
count_of_apple = fruits.count("apple")
print(f"\n..... \n There are {count_of_apple} apple in fruits tuple ")