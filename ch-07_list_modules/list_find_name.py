index = 0

def Find(name) :
    global index
    users = ["hari" , "shyam" , "ram"]
    if name.lower().strip() == users[index].lower() : 
        print("name matched" , index)
    index = index + 1
    if index < len(users) : Find(name)
    else : print("End of recursion")
    
    
