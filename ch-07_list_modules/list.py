index = 0

def Output() :
    global index
    users = [
        "mohit",
        "rahul",
        "saurav",
        "hari"
    ]
    print(users[index])
    index = index + 1
    if index < len(users) : Output()
    else : print("Recursion end")
    
Output()