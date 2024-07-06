def find(alpha) :
    if alpha == 'a' : return "for apple"
    elif alpha == 'b' : return "for ball"
    elif alpha == 'c' : return "for cat"
    elif alpha == 'd' : return "for dog"
    elif alpha == 'e' : return "for elephant"
    elif alpha == 'f' : return "for fan"
    elif alpha == 'g' : return "for god"
    elif alpha == 'h' : return "for horse"
    elif alpha == 'i' : return "for ice-cream"
    elif alpha == 'j' : return "for joker"
    elif alpha == 'k' : return "for king"
    elif alpha == 'l' : return "for lion"
    elif alpha == 'm' : return "for monkey"
    elif alpha == 'n' : return "for nest"
    elif alpha == 'o' : return "for orange"
    elif alpha == 'p' : return "for pink"
    elif alpha == 'q' : return "for queen"
    elif alpha == 'r' : return "for rat"
    elif alpha == 's' : return "for star"
    elif alpha == 't' : return "for t-shirt"
    elif alpha == 'u' : return "for umbrella"
    elif alpha == 'v' : return "for van"
    elif alpha == 'w' : return "for watch"
    elif alpha == 'x' : return "for x-ray"
    elif alpha == 'y' : return "for yak"
    elif alpha == 'z' : return "for zebra"
    else : return "not found"

    
    
def App() :
    print("Alpha-Phonix")
    print("-------------------------------")
    n = int(input("Enter times \n"))
    while n :
        alpha = input("Enter alpha\n")
        alpha = alpha.lower()
        result = find(alpha)
        print(alpha , result)
        n -= 1
    
App()