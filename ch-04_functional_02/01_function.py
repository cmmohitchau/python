name = "mohit"

# def wap() :
#     name = "hari"
#     print(name)
    
# def test() :
#     print(name)
    

# wap()
# test()


# using global keyword

def wap() :
    global name
    name = "hari"
    print(name)
    
def test() :
    print(name)
    

wap()
test()