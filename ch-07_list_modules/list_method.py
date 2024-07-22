#list is ordered, changeable and allow duplicates 
list = [1,2,3,"mohit",True]

# accessing elements
print(list[0])
print(list[1])
print(list[-1])

# Range of indexes
# last is not included like in [1:5] 5th index is not included
print(list[1:])
print(list[:len(list)])
print(list[3:5])

# check if item exists

if "mohit" in list : 
    print("yes it is included" , "\n.........")
else : 
    print("it is not included", "\n.........")
    
# changing elements
print("after changing elements\n............") 
list[1] = "ravi"
for i in range(0 , len(list)) :
    print(list[i])
    
# inserting elements
print("\n......\ninserting elements in (index , element)")
list.insert(1,"hero")
print(list[1])

# adding elements to the end
list.append("lastElement")
print("........\n printing last element")
print(list[len(list)-1])

# print("\nappending another list")
# list1 = ["super" , "awesome" , "wow"]
# list.append(list1)
# print(list)

# Extending list
# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).
list2 = ["cpu" , "mouse" , "monitor"]
list.extend(list2)
print("......\nafter extending\n" ,list)

# remove
list2.remove("mouse")
print(list2)

# pop
list2.pop(0)
print(list2)

# del and clear